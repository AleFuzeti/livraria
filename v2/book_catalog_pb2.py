# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book_catalog.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62ook_catalog.proto\x12\x06protos\"\x1c\n\x0b\x42ookRequest\x12\r\n\x05title\x18\x01 \x01(\t\"Y\n\x0c\x42ookResponse\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\r\n\x05stock\x18\x04 \x01(\x05\x12\r\n\x05price\x18\x05 \x01(\x02\"\x07\n\x05\x45mpty\"/\n\x08\x42ookList\x12#\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x14.protos.BookResponse2u\n\x0b\x42ookCatalog\x12\x38\n\x0bGetBookInfo\x12\x13.protos.BookRequest\x1a\x14.protos.BookResponse\x12,\n\tListBooks\x12\r.protos.Empty\x1a\x10.protos.BookListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_catalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOOKREQUEST']._serialized_start=30
  _globals['_BOOKREQUEST']._serialized_end=58
  _globals['_BOOKRESPONSE']._serialized_start=60
  _globals['_BOOKRESPONSE']._serialized_end=149
  _globals['_EMPTY']._serialized_start=151
  _globals['_EMPTY']._serialized_end=158
  _globals['_BOOKLIST']._serialized_start=160
  _globals['_BOOKLIST']._serialized_end=207
  _globals['_BOOKCATALOG']._serialized_start=209
  _globals['_BOOKCATALOG']._serialized_end=326
# @@protoc_insertion_point(module_scope)