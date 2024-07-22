from flask import Flask, request, jsonify, session, render_template
import grpc
import book_catalog_pb2
import book_catalog_pb2_grpc
import order_management_pb2
import order_management_pb2_grpc
import user_auth_pb2
import user_auth_pb2_grpc

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Funções para obter stubs singleton
def get_book_catalog_stub():
    if not hasattr(get_book_catalog_stub, "_stub"):
        book_catalog_channel = grpc.insecure_channel('localhost:50051')
        get_book_catalog_stub._stub = book_catalog_pb2_grpc.BookCatalogStub(book_catalog_channel)
    return get_book_catalog_stub._stub

def get_order_management_stub():
    if not hasattr(get_order_management_stub, "_stub"):
        order_management_channel = grpc.insecure_channel('localhost:50052')
        get_order_management_stub._stub = order_management_pb2_grpc.OrderManagementStub(order_management_channel)
    return get_order_management_stub._stub

def get_user_auth_stub():
    if not hasattr(get_user_auth_stub, "_stub"):
        user_auth_channel = grpc.insecure_channel('localhost:50053')
        get_user_auth_stub._stub = user_auth_pb2_grpc.UserAuthStub(user_auth_channel)
    return get_user_auth_stub._stub

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    stub = get_user_auth_stub()
    try:
        response = stub.RegisterUser(user_auth_pb2.UserCredentials(username=data['username'], password=data['password']))
        return jsonify({"token": response.token})
    except grpc.RpcError as e:
        return jsonify({"error": f"Registration failed: {e.details()}"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    stub = get_user_auth_stub()
    try:
        response = stub.LoginUser(user_auth_pb2.UserCredentials(username=data['username'], password=data['password']))
        if response.token:
            session['token'] = response.token
            session['user_id'] = data['username']  # Assuming username is the user_id
            return jsonify({"token": response.token})
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except grpc.RpcError as e:
        return jsonify({"error": f"Login failed: {e.details()}"}), 400

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    stub = get_book_catalog_stub()
    try:
        response = stub.GetBookInfo(book_catalog_pb2.BookRequest(title=title))
        if response.title:
            return jsonify({
                "title": response.title,
                "author": response.author,
                "year": response.year,
                "stock": response.stock,
                "price": response.price
            })
        else:
            return jsonify({"error": "Book not found"}), 404
    except grpc.RpcError as e:
        return jsonify({"error": f"Failed to retrieve book: {e.details()}"}), 500

@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "User not logged in"}), 401

    book_stub = get_book_catalog_stub()
    order_stub = get_order_management_stub()
    try:
        quantity = int(data['quantity'])  # Converter quantidade para inteiro

        # Primeiro, obter o preço do livro
        book_response = book_stub.GetBookInfo(book_catalog_pb2.BookRequest(title=data['title']))
        if not book_response.title:
            return jsonify({"error": "Book not found"}), 404

        # Calcular o preço total
        total_price = book_response.price * quantity

        # Fazer o pedido
        order_response = order_stub.PlaceOrder(
            order_management_pb2.OrderRequest(title=data['title'], quantity=quantity, user_id=user_id)
        )

        return jsonify({
            "order_id": order_response.order_id,
            "total_price": total_price  # Adiciona o preço total na resposta
        })
    except ValueError:
        return jsonify({"error": "Quantity must be an integer"}), 400
    except grpc.RpcError as e:
        return jsonify({"error": f"Failed to place order: {e.details()}"}), 500

@app.route('/order/<order_id>', methods=['GET'])
def get_order_details(order_id):
    stub = get_order_management_stub()
    try:
        response = stub.GetOrderDetails(order_management_pb2.OrderIdRequest(order_id=order_id))
        return jsonify({
            "title": response.title,
            "quantity": response.quantity,
            "order_date": response.order_date,
            "total_price": response.total_price
        })
    except grpc.RpcError as e:
        return jsonify({"error": f"Failed to retrieve order details: {e.details()}"}), 500

@app.route('/order/history', methods=['GET'])
def get_order_history():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "User not logged in"}), 401

    stub = get_order_management_stub()
    try:
        response = stub.GetOrderHistory(order_management_pb2.UserRequest(user_id=user_id))
        titles_list = list(response.titles)
        return jsonify({"titles": titles_list})
    except grpc.RpcError as e:
        return jsonify({"error": f"Failed to retrieve order history: {e.details()}"}), 500

if __name__ == '__main__':
    app.run(port=8080, debug=True)
