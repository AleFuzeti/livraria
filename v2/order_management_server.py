import grpc
from concurrent import futures
import order_management_pb2 as order_management_pb2
import order_management_pb2_grpc as order_management_pb2_grpc
from datetime import datetime

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.orders = {}  # Dicionário para armazenar pedidos
        self.order_id_counter = 1

    def PlaceOrder(self, request, context):
        order_id = str(self.order_id_counter)
        self.order_id_counter += 1
        self.orders[order_id] = {
            "title": request.title,
            "quantity": request.quantity,
            "user_id": request.user_id,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return order_management_pb2.OrderResponse(order_id=order_id)

    def GetOrderDetails(self, request, context):
        order = self.orders.get(request.order_id, None)
        if order:
            return order_management_pb2.OrderDetails(
                order_id=request.order_id,
                title=order["title"],
                quantity=order["quantity"],
                date=order["date"]
            )
        else:
            context.set_details("Order not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return order_management_pb2.OrderDetails()

    def GetOrderHistory(self, request, context):
        titles = [order["title"] for order in self.orders.values() if order["user_id"] == request.user_id]
        return order_management_pb2.OrderHistory(titles=titles)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
