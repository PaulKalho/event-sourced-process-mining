# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/services/property_svc/v1/property_value_svc.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.services.property_svc.v1 import types_pb2 as proto_dot_services_dot_property__svc_dot_v1_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7proto/services/property_svc/v1/property_value_svc.proto\x12\x1eproto.services.property_svc.v1\x1a*proto/services/property_svc/v1/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfe\x02\n\x1a\x41ttachPropertyValueRequest\x12\x1d\n\nsubject_id\x18\x01 \x01(\tR\tsubjectId\x12\x1f\n\x0bproperty_id\x18\x02 \x01(\tR\npropertyId\x12\x1f\n\ntext_value\x18\x03 \x01(\tH\x00R\ttextValue\x12#\n\x0cnumber_value\x18\x04 \x01(\x01H\x00R\x0bnumberValue\x12\x1f\n\nbool_value\x18\x05 \x01(\x08H\x00R\tboolValue\x12\x45\n\ndate_value\x18\x06 \x01(\x0b\x32$.proto.services.property_svc.v1.DateH\x00R\tdateValue\x12\x44\n\x0f\x64\x61te_time_value\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\rdateTimeValue\x12#\n\x0cselect_value\x18\x08 \x01(\tH\x00R\x0bselectValueB\x07\n\x05value\"I\n\x1b\x41ttachPropertyValueResponse\x12*\n\x11property_value_id\x18\x01 \x01(\tR\x0fpropertyValueId\"i\n\x13TaskPropertyMatcher\x12\x1c\n\x07ward_id\x18\x01 \x01(\tH\x00R\x06wardId\x88\x01\x01\x12\x1c\n\x07task_id\x18\x02 \x01(\tH\x01R\x06taskId\x88\x01\x01\x42\n\n\x08_ward_idB\n\n\x08_task_id\"\x87\x01\n GetAttachedPropertyValuesRequest\x12X\n\x0ctask_matcher\x18\x01 \x01(\x0b\x32\x33.proto.services.property_svc.v1.TaskPropertyMatcherH\x00R\x0btaskMatcherB\t\n\x07matcher\"\x87\x05\n!GetAttachedPropertyValuesResponse\x12_\n\x06values\x18\x01 \x03(\x0b\x32G.proto.services.property_svc.v1.GetAttachedPropertyValuesResponse.ValueR\x06values\x1a\x80\x04\n\x05Value\x12\x1f\n\x0bproperty_id\x18\x01 \x01(\tR\npropertyId\x12H\n\nfield_type\x18\x02 \x01(\x0e\x32).proto.services.property_svc.v1.FieldTypeR\tfieldType\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12%\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x01R\x0b\x64\x65scription\x88\x01\x01\x12\x1f\n\x0bis_archived\x18\x05 \x01(\x08R\nisArchived\x12\x1f\n\ntext_value\x18\x06 \x01(\tH\x00R\ttextValue\x12#\n\x0cnumber_value\x18\x07 \x01(\x01H\x00R\x0bnumberValue\x12\x1f\n\nbool_value\x18\x08 \x01(\x08H\x00R\tboolValue\x12\x45\n\ndate_value\x18\t \x01(\x0b\x32$.proto.services.property_svc.v1.DateH\x00R\tdateValue\x12\x44\n\x0f\x64\x61te_time_value\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\rdateTimeValue\x12#\n\x0cselect_value\x18\x0b \x01(\tH\x00R\x0bselectValueB\x07\n\x05valueB\x0e\n\x0c_description2\xce\x02\n\x14PropertyValueService\x12\x90\x01\n\x13\x41ttachPropertyValue\x12:.proto.services.property_svc.v1.AttachPropertyValueRequest\x1a;.proto.services.property_svc.v1.AttachPropertyValueResponse\"\x00\x12\xa2\x01\n\x19GetAttachedPropertyValues\x12@.proto.services.property_svc.v1.GetAttachedPropertyValuesRequest\x1a\x41.proto.services.property_svc.v1.GetAttachedPropertyValuesResponse\"\x00\x42\xf3\x01\n\"com.proto.services.property_svc.v1B\x15PropertyValueSvcProtoP\x01Z\x1fgen/proto/services/property-svc\xa2\x02\x03PSP\xaa\x02\x1dProto.Services.PropertySvc.V1\xca\x02\x1dProto\\Services\\PropertySvc\\V1\xe2\x02)Proto\\Services\\PropertySvc\\V1\\GPBMetadata\xea\x02 Proto::Services::PropertySvc::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.services.property_svc.v1.property_value_svc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.proto.services.property_svc.v1B\025PropertyValueSvcProtoP\001Z\037gen/proto/services/property-svc\242\002\003PSP\252\002\035Proto.Services.PropertySvc.V1\312\002\035Proto\\Services\\PropertySvc\\V1\342\002)Proto\\Services\\PropertySvc\\V1\\GPBMetadata\352\002 Proto::Services::PropertySvc::V1'
  _globals['_ATTACHPROPERTYVALUEREQUEST']._serialized_start=169
  _globals['_ATTACHPROPERTYVALUEREQUEST']._serialized_end=551
  _globals['_ATTACHPROPERTYVALUERESPONSE']._serialized_start=553
  _globals['_ATTACHPROPERTYVALUERESPONSE']._serialized_end=626
  _globals['_TASKPROPERTYMATCHER']._serialized_start=628
  _globals['_TASKPROPERTYMATCHER']._serialized_end=733
  _globals['_GETATTACHEDPROPERTYVALUESREQUEST']._serialized_start=736
  _globals['_GETATTACHEDPROPERTYVALUESREQUEST']._serialized_end=871
  _globals['_GETATTACHEDPROPERTYVALUESRESPONSE']._serialized_start=874
  _globals['_GETATTACHEDPROPERTYVALUESRESPONSE']._serialized_end=1521
  _globals['_GETATTACHEDPROPERTYVALUESRESPONSE_VALUE']._serialized_start=1009
  _globals['_GETATTACHEDPROPERTYVALUESRESPONSE_VALUE']._serialized_end=1521
  _globals['_PROPERTYVALUESERVICE']._serialized_start=1524
  _globals['_PROPERTYVALUESERVICE']._serialized_end=1858
# @@protoc_insertion_point(module_scope)
