import grpc
import book_catalog_pb2 as book_catalog_pb2
import book_catalog_pb2_grpc as book_catalog_pb2_grpc
import order_management_pb2 as order_management_pb2
import order_management_pb2_grpc as order_management_pb2_grpc
import user_auth_pb2 as user_auth_pb2
import user_auth_pb2_grpc as user_auth_pb2_grpc

def run():
    # Conectar aos serviços gRPC
    with grpc.insecure_channel('localhost:50051') as catalog_channel, \
         grpc.insecure_channel('localhost:50052') as order_channel, \
         grpc.insecure_channel('localhost:50053') as auth_channel:

        # Criar stubs para os serviços
        catalog_stub = book_catalog_pb2_grpc.BookCatalogStub(catalog_channel)
        order_stub = order_management_pb2_grpc.OrderManagementStub(order_channel)
        auth_stub = user_auth_pb2_grpc.UserAuthStub(auth_channel)

        # Registrar um novo usuário
        register_response = auth_stub.RegisterUser(user_auth_pb2.RegisterUserRequest(
            username='user1', password='password1'
        ))
        if register_response.token:
            print(f"Usuário registrado com sucesso. Token: {register_response.token}")
        else:
            print("Falha no registro do usuário")

        # Fazer login
        login_response = auth_stub.LoginUser(user_auth_pb2.LoginUserRequest(
            username='user1', password='password1'
        ))
        if login_response.token:
            print(f"Login bem-sucedido. Token: {login_response.token}")
        else:
            print("Falha no login do usuário")
            return

        # Solicitar informações de um livro
        book_info_response = catalog_stub.GetBookInfo(book_catalog_pb2.BookRequest(
            title="Livro A"
        ))
        if book_info_response.title:
            print(f"Informações do Livro A: {book_info_response}")
        else:
            print("Livro A não encontrado")

        # Listar todos os livros
        book_list_response = catalog_stub.ListBooks(book_catalog_pb2.Empty())
        print("Lista de livros disponíveis:")
        for book in book_list_response.books:
            print(book)

        # Fazer um pedido
        order_response = order_stub.PlaceOrder(order_management_pb2.OrderRequest(
            title="Livro A", quantity=1, user_id='user1'
        ))
        if order_response.order_id:
            print(f"Pedido realizado com sucesso. ID do Pedido: {order_response.order_id}")
        else:
            print("Falha ao realizar o pedido")

        # Obter detalhes do pedido
        order_details_response = order_stub.GetOrderDetails(order_management_pb2.OrderID(
            order_id=order_response.order_id
        ))
        if order_details_response.order_id:
            print(f"Detalhes do Pedido: {order_details_response}")
        else:
            print("Detalhes do pedido não encontrados")

        # Obter histórico de pedidos
        order_history_response = order_stub.GetOrderHistory(order_management_pb2.UserRequest(
            user_id='user1'
        ))
        print("Histórico de Pedidos:")
        for title in order_history_response.titles:
            print(title)

if __name__ == '__main__':
    run()
