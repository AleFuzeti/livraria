# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_auth.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fuser_auth.proto\x12\x08userauth\"5\n\x0fUserCredentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1d\n\x0c\x41uthResponse\x12\r\n\x05token\x18\x01 \x01(\t2\x8d\x01\n\x08UserAuth\x12\x41\n\x0cRegisterUser\x12\x19.userauth.UserCredentials\x1a\x16.userauth.AuthResponse\x12>\n\tLoginUser\x12\x19.userauth.UserCredentials\x1a\x16.userauth.AuthResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERCREDENTIALS']._serialized_start=29
  _globals['_USERCREDENTIALS']._serialized_end=82
  _globals['_AUTHRESPONSE']._serialized_start=84
  _globals['_AUTHRESPONSE']._serialized_end=113
  _globals['_USERAUTH']._serialized_start=116
  _globals['_USERAUTH']._serialized_end=257
# @@protoc_insertion_point(module_scope)
