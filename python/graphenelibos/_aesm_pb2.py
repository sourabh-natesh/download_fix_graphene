# pylint: skip-file

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aesm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aesm.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\naesm.proto\"U\n\x0eGetTokenReqRaw\x12\x11\n\tsignature\x18\x01 \x02(\x0c\x12\x0b\n\x03key\x18\x02 \x02(\x0c\x12\x12\n\nattributes\x18\x03 \x02(\x0c\x12\x0f\n\x07timeout\x18\t \x02(\r\"+\n\x0bGetTokenReq\x12\x1c\n\x03req\x18\x03 \x02(\x0b\x32\x0f.GetTokenReqRaw\".\n\x0eGetTokenRetRaw\x12\r\n\x05\x65rror\x18\x01 \x02(\x05\x12\r\n\x05token\x18\x02 \x01(\x0c\"+\n\x0bGetTokenRet\x12\x1c\n\x03ret\x18\x03 \x02(\x0b\x32\x0f.GetTokenRetRaw')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETTOKENREQRAW = _descriptor.Descriptor(
  name='GetTokenReqRaw',
  full_name='GetTokenReqRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='GetTokenReqRaw.signature', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='GetTokenReqRaw.key', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='GetTokenReqRaw.attributes', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='GetTokenReqRaw.timeout', index=3,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=99,
)


_GETTOKENREQ = _descriptor.Descriptor(
  name='GetTokenReq',
  full_name='GetTokenReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='GetTokenReq.req', index=0,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=144,
)


_GETTOKENRETRAW = _descriptor.Descriptor(
  name='GetTokenRetRaw',
  full_name='GetTokenRetRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='GetTokenRetRaw.error', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='GetTokenRetRaw.token', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=192,
)


_GETTOKENRET = _descriptor.Descriptor(
  name='GetTokenRet',
  full_name='GetTokenRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='GetTokenRet.ret', index=0,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=237,
)

_GETTOKENREQ.fields_by_name['req'].message_type = _GETTOKENREQRAW
_GETTOKENRET.fields_by_name['ret'].message_type = _GETTOKENRETRAW
DESCRIPTOR.message_types_by_name['GetTokenReqRaw'] = _GETTOKENREQRAW
DESCRIPTOR.message_types_by_name['GetTokenReq'] = _GETTOKENREQ
DESCRIPTOR.message_types_by_name['GetTokenRetRaw'] = _GETTOKENRETRAW
DESCRIPTOR.message_types_by_name['GetTokenRet'] = _GETTOKENRET

GetTokenReqRaw = _reflection.GeneratedProtocolMessageType('GetTokenReqRaw', (_message.Message,), dict(
  DESCRIPTOR = _GETTOKENREQRAW,
  __module__ = 'aesm_pb2'
  # @@protoc_insertion_point(class_scope:GetTokenReqRaw)
  ))
_sym_db.RegisterMessage(GetTokenReqRaw)

GetTokenReq = _reflection.GeneratedProtocolMessageType('GetTokenReq', (_message.Message,), dict(
  DESCRIPTOR = _GETTOKENREQ,
  __module__ = 'aesm_pb2'
  # @@protoc_insertion_point(class_scope:GetTokenReq)
  ))
_sym_db.RegisterMessage(GetTokenReq)

GetTokenRetRaw = _reflection.GeneratedProtocolMessageType('GetTokenRetRaw', (_message.Message,), dict(
  DESCRIPTOR = _GETTOKENRETRAW,
  __module__ = 'aesm_pb2'
  # @@protoc_insertion_point(class_scope:GetTokenRetRaw)
  ))
_sym_db.RegisterMessage(GetTokenRetRaw)

GetTokenRet = _reflection.GeneratedProtocolMessageType('GetTokenRet', (_message.Message,), dict(
  DESCRIPTOR = _GETTOKENRET,
  __module__ = 'aesm_pb2'
  # @@protoc_insertion_point(class_scope:GetTokenRet)
  ))
_sym_db.RegisterMessage(GetTokenRet)


# @@protoc_insertion_point(module_scope)