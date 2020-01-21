# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesh/v1alpha1/proxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from networking.v1alpha3 import destination_rule_pb2 as networking_dot_v1alpha3_dot_destination__rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mesh/v1alpha1/proxy.proto',
  package='istio.mesh.v1alpha1',
  syntax='proto3',
  serialized_options=_b('Z\032istio.io/api/mesh/v1alpha1'),
  serialized_pb=_b('\n\x19mesh/v1alpha1/proxy.proto\x12\x13istio.mesh.v1alpha1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a*networking/v1alpha3/destination_rule.proto\"\xf2\x04\n\x07Tracing\x12\x35\n\x06zipkin\x18\x01 \x01(\x0b\x32#.istio.mesh.v1alpha1.Tracing.ZipkinH\x00\x12;\n\tlightstep\x18\x02 \x01(\x0b\x32&.istio.mesh.v1alpha1.Tracing.LightstepH\x00\x12\x37\n\x07\x64\x61tadog\x18\x03 \x01(\x0b\x32$.istio.mesh.v1alpha1.Tracing.DatadogH\x00\x12?\n\x0bstackdriver\x18\x04 \x01(\x0b\x32(.istio.mesh.v1alpha1.Tracing.StackdriverH\x00\x1a\x19\n\x06Zipkin\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x1aW\n\tLightstep\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x0e\n\x06secure\x18\x03 \x01(\x08\x12\x13\n\x0b\x63\x61\x63\x65rt_path\x18\x04 \x01(\t\x1a\x1a\n\x07\x44\x61tadog\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x1a\xde\x01\n\x0bStackdriver\x12\r\n\x05\x64\x65\x62ug\x18\x01 \x01(\x08\x12=\n\x18max_number_of_attributes\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_number_of_annotations\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x41\n\x1cmax_number_of_message_events\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\n\x06tracer\"/\n\x03SDS\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x17\n\x0fk8s_sa_jwt_path\x18\x02 \x01(\t\"\x97\t\n\x0bProxyConfig\x12\x13\n\x0b\x63onfig_path\x18\x01 \x01(\t\x12\x13\n\x0b\x62inary_path\x18\x02 \x01(\t\x12\x17\n\x0fservice_cluster\x18\x03 \x01(\t\x12\x31\n\x0e\x64rain_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12;\n\x18parent_shutdown_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x19\n\x11\x64iscovery_address\x18\x06 \x01(\t\x12>\n\x17\x64iscovery_refresh_delay\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationB\x02\x18\x01\x12\x1a\n\x0ezipkin_address\x18\x08 \x01(\tB\x02\x18\x01\x12\x32\n\x0f\x63onnect_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1a\n\x12statsd_udp_address\x18\n \x01(\t\x12)\n\x1d\x65nvoy_metrics_service_address\x18\x14 \x01(\tB\x02\x18\x01\x12\x18\n\x10proxy_admin_port\x18\x0b \x01(\x05\x12\x1d\n\x11\x61vailability_zone\x18\x0c \x01(\tB\x02\x18\x01\x12L\n\x19\x63ontrol_plane_auth_policy\x18\r \x01(\x0e\x32).istio.mesh.v1alpha1.AuthenticationPolicy\x12\x1a\n\x12\x63ustom_config_file\x18\x0e \x01(\t\x12\x18\n\x10stat_name_length\x18\x0f \x01(\x05\x12\x13\n\x0b\x63oncurrency\x18\x10 \x01(\x05\x12%\n\x1dproxy_bootstrap_template_path\x18\x11 \x01(\t\x12S\n\x11interception_mode\x18\x12 \x01(\x0e\x32\x38.istio.mesh.v1alpha1.ProxyConfig.InboundInterceptionMode\x12-\n\x07tracing\x18\x13 \x01(\x0b\x32\x1c.istio.mesh.v1alpha1.Tracing\x12%\n\x03sds\x18\x15 \x01(\x0b\x32\x18.istio.mesh.v1alpha1.SDS\x12\x44\n\x18\x65nvoy_access_log_service\x18\x16 \x01(\x0b\x32\".istio.mesh.v1alpha1.RemoteService\x12\x41\n\x15\x65nvoy_metrics_service\x18\x17 \x01(\x0b\x32\".istio.mesh.v1alpha1.RemoteService\x12K\n\x0eproxy_metadata\x18\x18 \x03(\x0b\x32\x33.istio.mesh.v1alpha1.ProxyConfig.ProxyMetadataEntry\x1a\x34\n\x12ProxyMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"3\n\x17InboundInterceptionMode\x12\x0c\n\x08REDIRECT\x10\x00\x12\n\n\x06TPROXY\x10\x01\"\xc1\x01\n\rRemoteService\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12<\n\x0ctls_settings\x18\x02 \x01(\x0b\x32&.istio.networking.v1alpha3.TLSSettings\x12\x61\n\rtcp_keepalive\x18\x03 \x01(\x0b\x32J.istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings.TcpKeepalive*>\n\x14\x41uthenticationPolicy\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nMUTUAL_TLS\x10\x01\x12\x0c\n\x07INHERIT\x10\xe8\x07\x42\x1cZ\x1aistio.io/api/mesh/v1alpha1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,networking_dot_v1alpha3_dot_destination__rule__pb2.DESCRIPTOR,])

_AUTHENTICATIONPOLICY = _descriptor.EnumDescriptor(
  name='AuthenticationPolicy',
  full_name='istio.mesh.v1alpha1.AuthenticationPolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUTUAL_TLS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INHERIT', index=2, number=1000,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2210,
  serialized_end=2272,
)
_sym_db.RegisterEnumDescriptor(_AUTHENTICATIONPOLICY)

AuthenticationPolicy = enum_type_wrapper.EnumTypeWrapper(_AUTHENTICATIONPOLICY)
NONE = 0
MUTUAL_TLS = 1
INHERIT = 1000


_PROXYCONFIG_INBOUNDINTERCEPTIONMODE = _descriptor.EnumDescriptor(
  name='InboundInterceptionMode',
  full_name='istio.mesh.v1alpha1.ProxyConfig.InboundInterceptionMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REDIRECT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPROXY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1961,
  serialized_end=2012,
)
_sym_db.RegisterEnumDescriptor(_PROXYCONFIG_INBOUNDINTERCEPTIONMODE)


_TRACING_ZIPKIN = _descriptor.Descriptor(
  name='Zipkin',
  full_name='istio.mesh.v1alpha1.Tracing.Zipkin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='istio.mesh.v1alpha1.Tracing.Zipkin.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=408,
  serialized_end=433,
)

_TRACING_LIGHTSTEP = _descriptor.Descriptor(
  name='Lightstep',
  full_name='istio.mesh.v1alpha1.Tracing.Lightstep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='istio.mesh.v1alpha1.Tracing.Lightstep.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='istio.mesh.v1alpha1.Tracing.Lightstep.access_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secure', full_name='istio.mesh.v1alpha1.Tracing.Lightstep.secure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacert_path', full_name='istio.mesh.v1alpha1.Tracing.Lightstep.cacert_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=435,
  serialized_end=522,
)

_TRACING_DATADOG = _descriptor.Descriptor(
  name='Datadog',
  full_name='istio.mesh.v1alpha1.Tracing.Datadog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='istio.mesh.v1alpha1.Tracing.Datadog.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=524,
  serialized_end=550,
)

_TRACING_STACKDRIVER = _descriptor.Descriptor(
  name='Stackdriver',
  full_name='istio.mesh.v1alpha1.Tracing.Stackdriver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='debug', full_name='istio.mesh.v1alpha1.Tracing.Stackdriver.debug', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_number_of_attributes', full_name='istio.mesh.v1alpha1.Tracing.Stackdriver.max_number_of_attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_number_of_annotations', full_name='istio.mesh.v1alpha1.Tracing.Stackdriver.max_number_of_annotations', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_number_of_message_events', full_name='istio.mesh.v1alpha1.Tracing.Stackdriver.max_number_of_message_events', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=553,
  serialized_end=775,
)

_TRACING = _descriptor.Descriptor(
  name='Tracing',
  full_name='istio.mesh.v1alpha1.Tracing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zipkin', full_name='istio.mesh.v1alpha1.Tracing.zipkin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lightstep', full_name='istio.mesh.v1alpha1.Tracing.lightstep', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datadog', full_name='istio.mesh.v1alpha1.Tracing.datadog', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stackdriver', full_name='istio.mesh.v1alpha1.Tracing.stackdriver', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRACING_ZIPKIN, _TRACING_LIGHTSTEP, _TRACING_DATADOG, _TRACING_STACKDRIVER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='tracer', full_name='istio.mesh.v1alpha1.Tracing.tracer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=159,
  serialized_end=785,
)


_SDS = _descriptor.Descriptor(
  name='SDS',
  full_name='istio.mesh.v1alpha1.SDS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='istio.mesh.v1alpha1.SDS.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k8s_sa_jwt_path', full_name='istio.mesh.v1alpha1.SDS.k8s_sa_jwt_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=787,
  serialized_end=834,
)


_PROXYCONFIG_PROXYMETADATAENTRY = _descriptor.Descriptor(
  name='ProxyMetadataEntry',
  full_name='istio.mesh.v1alpha1.ProxyConfig.ProxyMetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mesh.v1alpha1.ProxyConfig.ProxyMetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mesh.v1alpha1.ProxyConfig.ProxyMetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1907,
  serialized_end=1959,
)

_PROXYCONFIG = _descriptor.Descriptor(
  name='ProxyConfig',
  full_name='istio.mesh.v1alpha1.ProxyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_path', full_name='istio.mesh.v1alpha1.ProxyConfig.config_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary_path', full_name='istio.mesh.v1alpha1.ProxyConfig.binary_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_cluster', full_name='istio.mesh.v1alpha1.ProxyConfig.service_cluster', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drain_duration', full_name='istio.mesh.v1alpha1.ProxyConfig.drain_duration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_shutdown_duration', full_name='istio.mesh.v1alpha1.ProxyConfig.parent_shutdown_duration', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_address', full_name='istio.mesh.v1alpha1.ProxyConfig.discovery_address', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_refresh_delay', full_name='istio.mesh.v1alpha1.ProxyConfig.discovery_refresh_delay', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zipkin_address', full_name='istio.mesh.v1alpha1.ProxyConfig.zipkin_address', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connect_timeout', full_name='istio.mesh.v1alpha1.ProxyConfig.connect_timeout', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statsd_udp_address', full_name='istio.mesh.v1alpha1.ProxyConfig.statsd_udp_address', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='envoy_metrics_service_address', full_name='istio.mesh.v1alpha1.ProxyConfig.envoy_metrics_service_address', index=10,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_admin_port', full_name='istio.mesh.v1alpha1.ProxyConfig.proxy_admin_port', index=11,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='availability_zone', full_name='istio.mesh.v1alpha1.ProxyConfig.availability_zone', index=12,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_plane_auth_policy', full_name='istio.mesh.v1alpha1.ProxyConfig.control_plane_auth_policy', index=13,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_config_file', full_name='istio.mesh.v1alpha1.ProxyConfig.custom_config_file', index=14,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stat_name_length', full_name='istio.mesh.v1alpha1.ProxyConfig.stat_name_length', index=15,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concurrency', full_name='istio.mesh.v1alpha1.ProxyConfig.concurrency', index=16,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_bootstrap_template_path', full_name='istio.mesh.v1alpha1.ProxyConfig.proxy_bootstrap_template_path', index=17,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interception_mode', full_name='istio.mesh.v1alpha1.ProxyConfig.interception_mode', index=18,
      number=18, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracing', full_name='istio.mesh.v1alpha1.ProxyConfig.tracing', index=19,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sds', full_name='istio.mesh.v1alpha1.ProxyConfig.sds', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='envoy_access_log_service', full_name='istio.mesh.v1alpha1.ProxyConfig.envoy_access_log_service', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='envoy_metrics_service', full_name='istio.mesh.v1alpha1.ProxyConfig.envoy_metrics_service', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_metadata', full_name='istio.mesh.v1alpha1.ProxyConfig.proxy_metadata', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROXYCONFIG_PROXYMETADATAENTRY, ],
  enum_types=[
    _PROXYCONFIG_INBOUNDINTERCEPTIONMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=837,
  serialized_end=2012,
)


_REMOTESERVICE = _descriptor.Descriptor(
  name='RemoteService',
  full_name='istio.mesh.v1alpha1.RemoteService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='istio.mesh.v1alpha1.RemoteService.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_settings', full_name='istio.mesh.v1alpha1.RemoteService.tls_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcp_keepalive', full_name='istio.mesh.v1alpha1.RemoteService.tcp_keepalive', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=2015,
  serialized_end=2208,
)

_TRACING_ZIPKIN.containing_type = _TRACING
_TRACING_LIGHTSTEP.containing_type = _TRACING
_TRACING_DATADOG.containing_type = _TRACING
_TRACING_STACKDRIVER.fields_by_name['max_number_of_attributes'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TRACING_STACKDRIVER.fields_by_name['max_number_of_annotations'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TRACING_STACKDRIVER.fields_by_name['max_number_of_message_events'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_TRACING_STACKDRIVER.containing_type = _TRACING
_TRACING.fields_by_name['zipkin'].message_type = _TRACING_ZIPKIN
_TRACING.fields_by_name['lightstep'].message_type = _TRACING_LIGHTSTEP
_TRACING.fields_by_name['datadog'].message_type = _TRACING_DATADOG
_TRACING.fields_by_name['stackdriver'].message_type = _TRACING_STACKDRIVER
_TRACING.oneofs_by_name['tracer'].fields.append(
  _TRACING.fields_by_name['zipkin'])
_TRACING.fields_by_name['zipkin'].containing_oneof = _TRACING.oneofs_by_name['tracer']
_TRACING.oneofs_by_name['tracer'].fields.append(
  _TRACING.fields_by_name['lightstep'])
_TRACING.fields_by_name['lightstep'].containing_oneof = _TRACING.oneofs_by_name['tracer']
_TRACING.oneofs_by_name['tracer'].fields.append(
  _TRACING.fields_by_name['datadog'])
_TRACING.fields_by_name['datadog'].containing_oneof = _TRACING.oneofs_by_name['tracer']
_TRACING.oneofs_by_name['tracer'].fields.append(
  _TRACING.fields_by_name['stackdriver'])
_TRACING.fields_by_name['stackdriver'].containing_oneof = _TRACING.oneofs_by_name['tracer']
_PROXYCONFIG_PROXYMETADATAENTRY.containing_type = _PROXYCONFIG
_PROXYCONFIG.fields_by_name['drain_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PROXYCONFIG.fields_by_name['parent_shutdown_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PROXYCONFIG.fields_by_name['discovery_refresh_delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PROXYCONFIG.fields_by_name['connect_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PROXYCONFIG.fields_by_name['control_plane_auth_policy'].enum_type = _AUTHENTICATIONPOLICY
_PROXYCONFIG.fields_by_name['interception_mode'].enum_type = _PROXYCONFIG_INBOUNDINTERCEPTIONMODE
_PROXYCONFIG.fields_by_name['tracing'].message_type = _TRACING
_PROXYCONFIG.fields_by_name['sds'].message_type = _SDS
_PROXYCONFIG.fields_by_name['envoy_access_log_service'].message_type = _REMOTESERVICE
_PROXYCONFIG.fields_by_name['envoy_metrics_service'].message_type = _REMOTESERVICE
_PROXYCONFIG.fields_by_name['proxy_metadata'].message_type = _PROXYCONFIG_PROXYMETADATAENTRY
_PROXYCONFIG_INBOUNDINTERCEPTIONMODE.containing_type = _PROXYCONFIG
_REMOTESERVICE.fields_by_name['tls_settings'].message_type = networking_dot_v1alpha3_dot_destination__rule__pb2._TLSSETTINGS
_REMOTESERVICE.fields_by_name['tcp_keepalive'].message_type = networking_dot_v1alpha3_dot_destination__rule__pb2._CONNECTIONPOOLSETTINGS_TCPSETTINGS_TCPKEEPALIVE
DESCRIPTOR.message_types_by_name['Tracing'] = _TRACING
DESCRIPTOR.message_types_by_name['SDS'] = _SDS
DESCRIPTOR.message_types_by_name['ProxyConfig'] = _PROXYCONFIG
DESCRIPTOR.message_types_by_name['RemoteService'] = _REMOTESERVICE
DESCRIPTOR.enum_types_by_name['AuthenticationPolicy'] = _AUTHENTICATIONPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tracing = _reflection.GeneratedProtocolMessageType('Tracing', (_message.Message,), {

  'Zipkin' : _reflection.GeneratedProtocolMessageType('Zipkin', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_ZIPKIN,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Zipkin)
    })
  ,

  'Lightstep' : _reflection.GeneratedProtocolMessageType('Lightstep', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_LIGHTSTEP,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Lightstep)
    })
  ,

  'Datadog' : _reflection.GeneratedProtocolMessageType('Datadog', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_DATADOG,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Datadog)
    })
  ,

  'Stackdriver' : _reflection.GeneratedProtocolMessageType('Stackdriver', (_message.Message,), {
    'DESCRIPTOR' : _TRACING_STACKDRIVER,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing.Stackdriver)
    })
  ,
  'DESCRIPTOR' : _TRACING,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Tracing)
  })
_sym_db.RegisterMessage(Tracing)
_sym_db.RegisterMessage(Tracing.Zipkin)
_sym_db.RegisterMessage(Tracing.Lightstep)
_sym_db.RegisterMessage(Tracing.Datadog)
_sym_db.RegisterMessage(Tracing.Stackdriver)

SDS = _reflection.GeneratedProtocolMessageType('SDS', (_message.Message,), {
  'DESCRIPTOR' : _SDS,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.SDS)
  })
_sym_db.RegisterMessage(SDS)

ProxyConfig = _reflection.GeneratedProtocolMessageType('ProxyConfig', (_message.Message,), {

  'ProxyMetadataEntry' : _reflection.GeneratedProtocolMessageType('ProxyMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROXYCONFIG_PROXYMETADATAENTRY,
    '__module__' : 'mesh.v1alpha1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.ProxyConfig.ProxyMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _PROXYCONFIG,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.ProxyConfig)
  })
_sym_db.RegisterMessage(ProxyConfig)
_sym_db.RegisterMessage(ProxyConfig.ProxyMetadataEntry)

RemoteService = _reflection.GeneratedProtocolMessageType('RemoteService', (_message.Message,), {
  'DESCRIPTOR' : _REMOTESERVICE,
  '__module__' : 'mesh.v1alpha1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.RemoteService)
  })
_sym_db.RegisterMessage(RemoteService)


DESCRIPTOR._options = None
_PROXYCONFIG_PROXYMETADATAENTRY._options = None
_PROXYCONFIG.fields_by_name['discovery_refresh_delay']._options = None
_PROXYCONFIG.fields_by_name['zipkin_address']._options = None
_PROXYCONFIG.fields_by_name['envoy_metrics_service_address']._options = None
_PROXYCONFIG.fields_by_name['availability_zone']._options = None
# @@protoc_insertion_point(module_scope)
