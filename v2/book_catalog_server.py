import grpc
from concurrent import futures
import book_catalog_pb2 as book_catalog_pb2
import book_catalog_pb2_grpc as book_catalog_pb2_grpc

class BookCatalogServicer(book_catalog_pb2_grpc.BookCatalogServicer):
    def __init__(self):
        # Carregar livros de um arquivo txt
        self.books = self.load_books()

    def load_books(self):
        # Aqui você deve implementar a lógica para carregar os livros de um txt
        # Exemplo fictício
        return {
            "Livro A": {"author": "Autor A", "year": 2020, "stock": 10, "price": 49.99},
            "Livro B": {"author": "Autor B", "year": 2021, "stock": 5, "price": 59.99}
        }

    def GetBookInfo(self, request, context):
        book = self.books.get(request.title, None)
        if book:
            return book_catalog_pb2.BookResponse(
                title=request.title,
                author=book["author"],
                year=book["year"],
                stock=book["stock"],
                price=book["price"]
            )
        else:
            context.set_details("Book not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return book_catalog_pb2.BookResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_catalog_pb2_grpc.add_BookCatalogServicer_to_server(BookCatalogServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
