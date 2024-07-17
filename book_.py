from concurrent import futures
import grpc
import book_catalog_pb2
import book_catalog_pb2_grpc

class BookCatalogServicer(book_catalog_pb2_grpc.BookCatalogServicer):
    def __init__(self):
        self.books = [
            {'title': 'Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937, 'stock': 10, 'price': 29.99},
            {'title': 'Harry Potter', 'author': 'J. K. Rowling', 'year': 1997, 'stock': 5, 'price': 19.99},
            {'title': 'Percy  Jackson', 'author': 'Rick Riordan', 'year': 2010, 'stock': 8, 'price': 14.99},
        ]
    
    def GetBookInfo(self, request, context):
        for book in self.books:
            if book['title'] == request.title:
                return book_catalog_pb2.BookResponse(
                    title=book['title'], author=book['author'], year=book['year'], 
                    stock=book['stock'], price=book['price']
                )
        return book_catalog_pb2.BookResponse()
    
    def ListBooks(self, request, context):
        book_list = book_catalog_pb2.BookList()
        for book in self.books:
            book_list.books.add(
                title=book['title'], author=book['author'], year=book['year'], 
                stock=book['stock'], price=book['price']
            )
        return book_list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_catalog_pb2_grpc.add_BookCatalogServicer_to_server(BookCatalogServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
