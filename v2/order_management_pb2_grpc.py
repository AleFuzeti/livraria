# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import order_management_pb2 as order__management__pb2

GRPC_GENERATED_VERSION = '1.65.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in order_management_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class OrderManagementStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PlaceOrder = channel.unary_unary(
                '/protos.OrderManagement/PlaceOrder',
                request_serializer=order__management__pb2.OrderRequest.SerializeToString,
                response_deserializer=order__management__pb2.OrderResponse.FromString,
                _registered_method=True)
        self.GetOrderDetails = channel.unary_unary(
                '/protos.OrderManagement/GetOrderDetails',
                request_serializer=order__management__pb2.OrderID.SerializeToString,
                response_deserializer=order__management__pb2.OrderDetails.FromString,
                _registered_method=True)
        self.GetOrderHistory = channel.unary_unary(
                '/protos.OrderManagement/GetOrderHistory',
                request_serializer=order__management__pb2.UserRequest.SerializeToString,
                response_deserializer=order__management__pb2.OrderHistory.FromString,
                _registered_method=True)


class OrderManagementServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PlaceOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderManagementServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PlaceOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaceOrder,
                    request_deserializer=order__management__pb2.OrderRequest.FromString,
                    response_serializer=order__management__pb2.OrderResponse.SerializeToString,
            ),
            'GetOrderDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderDetails,
                    request_deserializer=order__management__pb2.OrderID.FromString,
                    response_serializer=order__management__pb2.OrderDetails.SerializeToString,
            ),
            'GetOrderHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderHistory,
                    request_deserializer=order__management__pb2.UserRequest.FromString,
                    response_serializer=order__management__pb2.OrderHistory.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.OrderManagement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('protos.OrderManagement', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OrderManagement(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PlaceOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/protos.OrderManagement/PlaceOrder',
            order__management__pb2.OrderRequest.SerializeToString,
            order__management__pb2.OrderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetOrderDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/protos.OrderManagement/GetOrderDetails',
            order__management__pb2.OrderID.SerializeToString,
            order__management__pb2.OrderDetails.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetOrderHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/protos.OrderManagement/GetOrderHistory',
            order__management__pb2.UserRequest.SerializeToString,
            order__management__pb2.OrderHistory.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
