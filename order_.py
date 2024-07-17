from concurrent import futures
import grpc
import order_management_pb2
import order_management_pb2_grpc
import uuid
from datetime import datetime

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.orders = {}

    def PlaceOrder(self, request, context):
        order_id = str(uuid.uuid4())
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.orders[order_id] = {
            'user_id': request.user_id,
            'items': request.items,
            'order_date': order_date
        }
        return order_management_pb2.OrderResponse(order_id=order_id)
    
    def GetOrderDetails(self, request, context):
        order = self.orders.get(request.order_id)
        if order:
            order_items = [
                order_management_pb2.OrderItem(title=item.title, quantity=item.quantity)
                for item in order['items']
            ]
            return order_management_pb2.OrderDetails(
                order_id=request.order_id, user_id=order['user_id'], 
                items=order_items, order_date=order['order_date']
            )
        return order_management_pb2.OrderDetails()
    
    def GetOrderHistory(self, request, context):
        order_history = order_management_pb2.OrderHistory()
        for order_id, order in self.orders.items():
            if order['user_id'] == request.user_id:
                titles = [item.title for item in order['items']]
                order_summary = order_management_pb2.OrderSummary(order_id=order_id, titles=titles)
                order_history.orders.append(order_summary)
        return order_history

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
