# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networking/v1alpha3/gateway_plugin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='networking/v1alpha3/gateway_plugin.proto',
  package='istio.networking.v1alpha3',
  syntax='proto3',
  serialized_options=_b('Z istio.io/api/networking/v1alpha3'),
  serialized_pb=_b('\n(networking/v1alpha3/gateway_plugin.proto\x12\x19istio.networking.v1alpha3\x1a\x1cgoogle/protobuf/struct.proto\"\xa9\x01\n\rGatewayPlugin\x12\r\n\x05route\x18\x01 \x03(\t\x12\x0c\n\x04host\x18\x02 \x03(\t\x12\x0f\n\x07service\x18\x03 \x03(\t\x12\x33\n\x07plugins\x18\x04 \x03(\x0b\x32\".istio.networking.v1alpha3.plugins\x12\x0f\n\x07gateway\x18\x05 \x03(\t\x12\x0c\n\x04user\x18\x06 \x03(\t\x12\x16\n\x0eisGroupSetting\x18\x07 \x01(\x08\"B\n\x07plugins\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x08settings\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\"Z istio.io/api/networking/v1alpha3b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GATEWAYPLUGIN = _descriptor.Descriptor(
  name='GatewayPlugin',
  full_name='istio.networking.v1alpha3.GatewayPlugin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route', full_name='istio.networking.v1alpha3.GatewayPlugin.route', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='istio.networking.v1alpha3.GatewayPlugin.host', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='istio.networking.v1alpha3.GatewayPlugin.service', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugins', full_name='istio.networking.v1alpha3.GatewayPlugin.plugins', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='istio.networking.v1alpha3.GatewayPlugin.gateway', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='istio.networking.v1alpha3.GatewayPlugin.user', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isGroupSetting', full_name='istio.networking.v1alpha3.GatewayPlugin.isGroupSetting', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=271,
)


_PLUGINS = _descriptor.Descriptor(
  name='plugins',
  full_name='istio.networking.v1alpha3.plugins',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.networking.v1alpha3.plugins.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='istio.networking.v1alpha3.plugins.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=339,
)

_GATEWAYPLUGIN.fields_by_name['plugins'].message_type = _PLUGINS
_PLUGINS.fields_by_name['settings'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['GatewayPlugin'] = _GATEWAYPLUGIN
DESCRIPTOR.message_types_by_name['plugins'] = _PLUGINS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GatewayPlugin = _reflection.GeneratedProtocolMessageType('GatewayPlugin', (_message.Message,), dict(
  DESCRIPTOR = _GATEWAYPLUGIN,
  __module__ = 'networking.v1alpha3.gateway_plugin_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.GatewayPlugin)
  ))
_sym_db.RegisterMessage(GatewayPlugin)

plugins = _reflection.GeneratedProtocolMessageType('plugins', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINS,
  __module__ = 'networking.v1alpha3.gateway_plugin_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.plugins)
  ))
_sym_db.RegisterMessage(plugins)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
