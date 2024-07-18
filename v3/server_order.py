from concurrent import futures
import grpc
import order_management_pb2
import order_management_pb2_grpc
import uuid
from datetime import datetime
import book_catalog_pb2
import book_catalog_pb2_grpc

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self, book_catalog_stub):
        self.orders = {}
        self.history = {}
        self.book_catalog_stub = book_catalog_stub

    def PlaceOrder(self, request, context):
        # Verificar estoque
        book_request = book_catalog_pb2.BookRequest(title=request.title)
        try:
            book_info = self.book_catalog_stub.GetBookInfo(book_request)
        except grpc.RpcError as e:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details(f'Failed to contact book catalog: {e.details()}')
            return order_management_pb2.OrderResponse()
        
        if book_info.stock < request.quantity:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details('Not enough stock')
            return order_management_pb2.OrderResponse()
        
        
        # Atualizar estoque
        print(book_info.stock - request.quantity)
        new_stock = book_info.stock - request.quantity
        update_stock_request = book_catalog_pb2.UpdateStockRequest(title=request.title, new_stock=new_stock)
        try:
            update_response = self.book_catalog_stub.UpdateBookStock(update_stock_request)
            if not update_response.success:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details('Failed to update book stock')
                return order_management_pb2.OrderResponse()
        except grpc.RpcError as e:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details(f'Failed to contact book catalog: {e.details()}')
            return order_management_pb2.OrderResponse()
        
        # Calcular preço total
        total_price = book_info.price * request.quantity

        order_id = str(uuid.uuid4())
        self.orders[order_id] = {
            "title": request.title,
            "quantity": request.quantity,
            "order_date": str(datetime.now()),
            "total_price": total_price
        }
        if request.user_id not in self.history:
            self.history[request.user_id] = []
        self.history[request.user_id].append(request.title)
        
        return order_management_pb2.OrderResponse(order_id=order_id)

    def GetOrderDetails(self, request, context):
        order = self.orders.get(request.order_id)
        if order:
            return order_management_pb2.OrderDetailsResponse(**order)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Order not found')
            return order_management_pb2.OrderDetailsResponse()

    def GetOrderHistory(self, request, context):
        titles = self.history.get(request.user_id, [])
        return order_management_pb2.OrderHistoryResponse(titles=titles)

def serve():
    book_catalog_channel = grpc.insecure_channel('localhost:50051')
    book_catalog_stub = book_catalog_pb2_grpc.BookCatalogStub(book_catalog_channel)
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(book_catalog_stub), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
