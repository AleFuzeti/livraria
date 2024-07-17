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

# Conexão com os serviços gRPC
book_catalog_channel = grpc.insecure_channel('localhost:50051')
book_catalog_stub = book_catalog_pb2_grpc.BookCatalogStub(book_catalog_channel)

order_management_channel = grpc.insecure_channel('localhost:50052')
order_management_stub = order_management_pb2_grpc.OrderManagementStub(order_management_channel)

user_auth_channel = grpc.insecure_channel('localhost:50053')
user_auth_stub = user_auth_pb2_grpc.UserAuthStub(user_auth_channel)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        response = user_auth_stub.RegisterUser(user_auth_pb2.UserCredentials(username=data['username'], password=data['password']))
        return jsonify({"token": response.token})
    except grpc.RpcError as e:
        return jsonify({"error": f"Registration failed: {e.details()}"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        response = user_auth_stub.LoginUser(user_auth_pb2.UserCredentials(username=data['username'], password=data['password']))
        if response.token:
            session['token'] = response.token
            return jsonify({"token": response.token})
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except grpc.RpcError as e:
        return jsonify({"error": f"Login failed: {e.details()}"}), 400


@app.route('/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    try:
        response = book_catalog_stub.GetBookInfo(book_catalog_pb2.BookRequest(title=title))
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
    response = order_management_stub.PlaceOrder(order_management_pb2.OrderRequest(title=data['title'], quantity=data['quantity'], user_id=data['user_id']))
    return jsonify({"order_id": response.order_id})

@app.route('/order/<order_id>', methods=['GET'])
def get_order_details(order_id):
    response = order_management_stub.GetOrderDetails(order_management_pb2.OrderIdRequest(order_id=order_id))
    return jsonify({"title": response.title, "quantity": response.quantity, "order_date": response.order_date})

@app.route('/order/history', methods=['GET'])
def get_order_history():
    user_id = request.args.get('user_id')
    response = order_management_stub.GetOrderHistory(order_management_pb2.UserRequest(user_id=user_id))
    return jsonify({"titles": response.titles})

if __name__ == '__main__':
    app.run(port=8080, debug=True)
