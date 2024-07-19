from concurrent import futures
import grpc
import book_catalog_pb2
import book_catalog_pb2_grpc
from singleton import Singleton  # Importe o Singleton

class BookCatalogServicer(book_catalog_pb2_grpc.BookCatalogServicer, Singleton):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.books = {
                "HarryPotter": {"title": "HarryPotter", "author": "JK Rowling", "year": 1998, "stock": 50, "price": 50.00},
                "PercyJackson": {"title": "PercyJackson", "author": "Rick Riordan", "year": 2011, "stock": 30, "price": 30.00},
                "PequenoPrincipe": {"title": "PequenoPrincipe", "author": "Antoine de Saint-Exupéry", "year": 1943, "stock": 20, "price": 20.00},
            }
            self.initialized = True

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
