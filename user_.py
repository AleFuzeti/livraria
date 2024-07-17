from concurrent import futures
import grpc
import user_authentication_pb2
import user_authentication_pb2_grpc
import uuid

class UserAuthenticationServicer(user_authentication_pb2_grpc.UserAuthenticationServicer):
    def __init__(self):
        self.users = {}
        self.sessions = {}

    def RegisterUser(self, request, context):
        user_id = str(uuid.uuid4())
        self.users[request.username] = {
            'password': request.password,
            'user_id': user_id
        }
        return user_authentication_pb2.AuthResponse(token=user_id, user_id=user_id)
    
    def LoginUser(self, request, context):
        user = self.users.get(request.username)
        if user and user['password'] == request.password:
            session_token = str(uuid.uuid4())
            self.sessions[session_token] = user['user_id']
            return user_authentication_pb2.AuthResponse(token=session_token, user_id=user['user_id'])
        return user_authentication_pb2.AuthResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_authentication_pb2_grpc.add_UserAuthenticationServicer_to_server(UserAuthenticationServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
