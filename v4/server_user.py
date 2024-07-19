from concurrent import futures
import grpc
import user_auth_pb2
import user_auth_pb2_grpc
import hashlib
from singleton import Singleton  # Importe o Singleton

class UserAuthServicer(user_auth_pb2_grpc.UserAuthServicer, Singleton):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.users = {}
            self.initialized = True

    def RegisterUser(self, request, context):
        if request.username in self.users:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details('User already exists')
            return user_auth_pb2.AuthResponse()
        self.users[request.username] = hashlib.sha256(request.password.encode()).hexdigest()
        return user_auth_pb2.AuthResponse(token="Register OK")

    def LoginUser(self, request, context):
        hashed_pw = hashlib.sha256(request.password.encode()).hexdigest()
        if self.users.get(request.username) == hashed_pw:
            return user_auth_pb2.AuthResponse(token="Login OK")
        else:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details('Invalid credentials')
            return user_auth_pb2.AuthResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_auth_pb2_grpc.add_UserAuthServicer_to_server(UserAuthServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
