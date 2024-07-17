/**
 * @fileoverview gRPC-Web generated client stub for bookstore
 * @enhanceable
 * @public
 */

// Code generated by protoc-gen-grpc-web. DO NOT EDIT.
// versions:
// 	protoc-gen-grpc-web v1.5.0
// 	protoc              v3.12.4
// source: order_management.proto


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.bookstore = require('./order_management_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.bookstore.OrderManagementClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname.replace(/\/+$/, '');

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.bookstore.OrderManagementPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname.replace(/\/+$/, '');

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.bookstore.OrderRequest,
 *   !proto.bookstore.OrderResponse>}
 */
const methodDescriptor_OrderManagement_PlaceOrder = new grpc.web.MethodDescriptor(
  '/bookstore.OrderManagement/PlaceOrder',
  grpc.web.MethodType.UNARY,
  proto.bookstore.OrderRequest,
  proto.bookstore.OrderResponse,
  /**
   * @param {!proto.bookstore.OrderRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.bookstore.OrderResponse.deserializeBinary
);


/**
 * @param {!proto.bookstore.OrderRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.bookstore.OrderResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.bookstore.OrderResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.bookstore.OrderManagementClient.prototype.placeOrder =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/bookstore.OrderManagement/PlaceOrder',
      request,
      metadata || {},
      methodDescriptor_OrderManagement_PlaceOrder,
      callback);
};


/**
 * @param {!proto.bookstore.OrderRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.bookstore.OrderResponse>}
 *     Promise that resolves to the response
 */
proto.bookstore.OrderManagementPromiseClient.prototype.placeOrder =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/bookstore.OrderManagement/PlaceOrder',
      request,
      metadata || {},
      methodDescriptor_OrderManagement_PlaceOrder);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.bookstore.OrderID,
 *   !proto.bookstore.OrderDetails>}
 */
const methodDescriptor_OrderManagement_GetOrderDetails = new grpc.web.MethodDescriptor(
  '/bookstore.OrderManagement/GetOrderDetails',
  grpc.web.MethodType.UNARY,
  proto.bookstore.OrderID,
  proto.bookstore.OrderDetails,
  /**
   * @param {!proto.bookstore.OrderID} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.bookstore.OrderDetails.deserializeBinary
);


/**
 * @param {!proto.bookstore.OrderID} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.bookstore.OrderDetails)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.bookstore.OrderDetails>|undefined}
 *     The XHR Node Readable Stream
 */
proto.bookstore.OrderManagementClient.prototype.getOrderDetails =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/bookstore.OrderManagement/GetOrderDetails',
      request,
      metadata || {},
      methodDescriptor_OrderManagement_GetOrderDetails,
      callback);
};


/**
 * @param {!proto.bookstore.OrderID} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.bookstore.OrderDetails>}
 *     Promise that resolves to the response
 */
proto.bookstore.OrderManagementPromiseClient.prototype.getOrderDetails =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/bookstore.OrderManagement/GetOrderDetails',
      request,
      metadata || {},
      methodDescriptor_OrderManagement_GetOrderDetails);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.bookstore.UserID,
 *   !proto.bookstore.OrderHistory>}
 */
const methodDescriptor_OrderManagement_GetOrderHistory = new grpc.web.MethodDescriptor(
  '/bookstore.OrderManagement/GetOrderHistory',
  grpc.web.MethodType.UNARY,
  proto.bookstore.UserID,
  proto.bookstore.OrderHistory,
  /**
   * @param {!proto.bookstore.UserID} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.bookstore.OrderHistory.deserializeBinary
);


/**
 * @param {!proto.bookstore.UserID} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.bookstore.OrderHistory)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.bookstore.OrderHistory>|undefined}
 *     The XHR Node Readable Stream
 */
proto.bookstore.OrderManagementClient.prototype.getOrderHistory =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/bookstore.OrderManagement/GetOrderHistory',
      request,
      metadata || {},
      methodDescriptor_OrderManagement_GetOrderHistory,
      callback);
};


/**
 * @param {!proto.bookstore.UserID} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.bookstore.OrderHistory>}
 *     Promise that resolves to the response
 */
proto.bookstore.OrderManagementPromiseClient.prototype.getOrderHistory =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/bookstore.OrderManagement/GetOrderHistory',
      request,
      metadata || {},
      methodDescriptor_OrderManagement_GetOrderHistory);
};


module.exports = proto.bookstore;

