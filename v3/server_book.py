from concurrent import futures
import grpc
import book_catalog_pb2
import book_catalog_pb2_grpc

class BookCatalogServicer(book_catalog_pb2_grpc.BookCatalogServicer):
    def __init__(self):
        self.books = {
            "Book1": {"title": "Book1", "author": "Author1", "year": 2001, "stock": 10, "price": 29.99},
            # Adicione outros livros aqui
        }

    def GetBookInfo(self, request, context):
        book = self.books.get(request.title)
        if book:
            return book_catalog_pb2.BookInfoResponse(**book)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Book not found')
            return book_catalog_pb2.BookInfoResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_catalog_pb2_grpc.add_BookCatalogServicer_to_server(BookCatalogServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
