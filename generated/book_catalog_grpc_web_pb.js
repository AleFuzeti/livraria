/**
 * @fileoverview gRPC-Web generated client stub for bookstore
 * @enhanceable
 * @public
 */

// Code generated by protoc-gen-grpc-web. DO NOT EDIT.
// versions:
// 	protoc-gen-grpc-web v1.5.0
// 	protoc              v3.12.4
// source: book_catalog.proto


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.bookstore = require('./book_catalog_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.bookstore.BookCatalogClient =
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
proto.bookstore.BookCatalogPromiseClient =
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
 *   !proto.bookstore.BookRequest,
 *   !proto.bookstore.BookResponse>}
 */
const methodDescriptor_BookCatalog_GetBookInfo = new grpc.web.MethodDescriptor(
  '/bookstore.BookCatalog/GetBookInfo',
  grpc.web.MethodType.UNARY,
  proto.bookstore.BookRequest,
  proto.bookstore.BookResponse,
  /**
   * @param {!proto.bookstore.BookRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.bookstore.BookResponse.deserializeBinary
);


/**
 * @param {!proto.bookstore.BookRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.bookstore.BookResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.bookstore.BookResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.bookstore.BookCatalogClient.prototype.getBookInfo =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/bookstore.BookCatalog/GetBookInfo',
      request,
      metadata || {},
      methodDescriptor_BookCatalog_GetBookInfo,
      callback);
};


/**
 * @param {!proto.bookstore.BookRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.bookstore.BookResponse>}
 *     Promise that resolves to the response
 */
proto.bookstore.BookCatalogPromiseClient.prototype.getBookInfo =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/bookstore.BookCatalog/GetBookInfo',
      request,
      metadata || {},
      methodDescriptor_BookCatalog_GetBookInfo);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.bookstore.Empty,
 *   !proto.bookstore.BookList>}
 */
const methodDescriptor_BookCatalog_ListBooks = new grpc.web.MethodDescriptor(
  '/bookstore.BookCatalog/ListBooks',
  grpc.web.MethodType.UNARY,
  proto.bookstore.Empty,
  proto.bookstore.BookList,
  /**
   * @param {!proto.bookstore.Empty} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.bookstore.BookList.deserializeBinary
);


/**
 * @param {!proto.bookstore.Empty} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.bookstore.BookList)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.bookstore.BookList>|undefined}
 *     The XHR Node Readable Stream
 */
proto.bookstore.BookCatalogClient.prototype.listBooks =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/bookstore.BookCatalog/ListBooks',
      request,
      metadata || {},
      methodDescriptor_BookCatalog_ListBooks,
      callback);
};


/**
 * @param {!proto.bookstore.Empty} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.bookstore.BookList>}
 *     Promise that resolves to the response
 */
proto.bookstore.BookCatalogPromiseClient.prototype.listBooks =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/bookstore.BookCatalog/ListBooks',
      request,
      metadata || {},
      methodDescriptor_BookCatalog_ListBooks);
};


module.exports = proto.bookstore;

