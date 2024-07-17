import grpc
import book_catalog_pb2
import book_catalog_pb2_grpc
import order_management_pb2
import order_management_pb2_grpc
import user_authentication_pb2
import user_authentication_pb2_grpc

def run():
    # Conectar ao serviço de catálogo de livros
    channel = grpc.insecure_channel('localhost:50051')
    book_stub = book_catalog_pb2_grpc.BookCatalogStub(channel)

    # Listar livros
    books = book_stub.ListBooks(book_catalog_pb2.Empty())
    for book in books.books:
        print(f'{book.title} by {book.author}, Price: ${book.price}')

    # Conectar ao serviço de autenticação de usuários
    auth_channel = grpc.insecure_channel('localhost:50053')
    auth_stub = user_authentication_pb2_grpc.UserAuthenticationStub(auth_channel)

    # Registrar e fazer login de um usuário
    user = user_authentication_pb2.RegisterRequest(username='test_user', password='password123')
    response = auth_stub.RegisterUser(user)
    print(f'User ID: {response.user_id}, Token: {response.token}')

    # Conectar ao serviço de gerenciamento de pedidos
    order_channel = grpc.insecure_channel('localhost:50052')
    order_stub = order_management_pb2_grpc.OrderManagementStub(order_channel)

    # Fazer um pedido
    order_request = order_management_pb2.OrderRequest(
        user_id=response.user_id,
        items=[order_management_pb2.OrderItem(title='Hobbit', quantity=1)]
    )
    order_response = order_stub.PlaceOrder(order_request)
    print(f'Order ID: {order_response.order_id}')

    # Obter detalhes do pedido
    order_details = order_stub.GetOrderDetails(order_management_pb2.OrderID(order_id=order_response.order_id))
    print(f'Order Details: {order_details}')

if __name__ == '__main__':
    run()

