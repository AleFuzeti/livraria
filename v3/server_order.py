from concurrent import futures
import grpc
import order_management_pb2
import order_management_pb2_grpc
import uuid
from datetime import datetime

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.orders = {}
        self.history = {}

    def PlaceOrder(self, request, context):
        order_id = str(uuid.uuid4())
        self.orders[order_id] = {
            "title": request.title,
            "quantity": request.quantity,
            "order_date": str(datetime.now())
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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
