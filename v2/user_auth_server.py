import grpc
from concurrent import futures
import user_auth_pb2 as user_auth_pb2
import user_auth_pb2_grpc as user_auth_pb2_grpc
import hashlib
import jwt

SECRET_KEY = "your_secret_key"

class UserAuthServicer(user_auth_pb2_grpc.UserAuthServicer):
    def __init__(self):
        self.users = {}  # Dicionário para armazenar usuários

    def RegisterUser(self, request, context):
        if request.username in self.users:
            context.set_details("Username already exists")
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            return user_auth_pb2.AuthResponse()

        hashed_password = hashlib.sha256(request.password.encode()).hexdigest()
        self.users[request.username] = hashed_password
        token = jwt.encode({"username": request.username}, SECRET_KEY, algorithm="HS256")
        return user_auth_pb2.AuthResponse(token=token)

    def LoginUser(self, request, context):
        hashed_password = hashlib.sha256(request.password.encode()).hexdigest()
        if self.users.get(request.username) == hashed_password:
            token = jwt.encode({"username": request.username}, SECRET_KEY, algorithm="HS256")
            return user_auth_pb2.AuthResponse(token=token)
        else:
            context.set_details("Invalid credentials")
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            return user_auth_pb2.AuthResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_auth_pb2_grpc.add_UserAuthServicer_to_server(UserAuthServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
