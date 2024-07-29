# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/services/task_svc/v1/bed_svc.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/services/task_svc/v1/bed_svc.proto\x12\x1aproto.services.task_svc.v1\"?\n\x10\x43reateBedRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"#\n\x11\x43reateBedResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"V\n\x15\x42ulkCreateBedsRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12$\n\x0e\x61mount_of_beds\x18\x02 \x01(\rR\x0c\x61mountOfBeds\"\x8f\x01\n\x16\x42ulkCreateBedsResponse\x12J\n\x04\x62\x65\x64s\x18\x01 \x03(\x0b\x32\x36.proto.services.task_svc.v1.BulkCreateBedsResponse.BedR\x04\x62\x65\x64s\x1a)\n\x03\x42\x65\x64\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\x1f\n\rGetBedRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"M\n\x0eGetBedResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x17\n\x07room_id\x18\x02 \x01(\tR\x06roomId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\"7\n\x16GetBedByPatientRequest\x12\x1d\n\npatient_id\x18\x01 \x01(\tR\tpatientId\"\xbd\x02\n\x17GetBedByPatientResponse\x12Q\n\x04room\x18\x01 \x01(\x0b\x32\x38.proto.services.task_svc.v1.GetBedByPatientResponse.RoomH\x00R\x04room\x88\x01\x01\x12N\n\x03\x62\x65\x64\x18\x02 \x01(\x0b\x32\x37.proto.services.task_svc.v1.GetBedByPatientResponse.BedH\x01R\x03\x62\x65\x64\x88\x01\x01\x1a\x43\n\x04Room\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x17\n\x07ward_id\x18\x03 \x01(\tR\x06wardId\x1a)\n\x03\x42\x65\x64\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04nameB\x07\n\x05_roomB\x06\n\x04_bed\"\x10\n\x0eGetBedsRequest\"\x9a\x01\n\x0fGetBedsResponse\x12\x43\n\x04\x62\x65\x64s\x18\x01 \x03(\x0b\x32/.proto.services.task_svc.v1.GetBedsResponse.BedR\x04\x62\x65\x64s\x1a\x42\n\x03\x42\x65\x64\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x17\n\x07room_id\x18\x02 \x01(\tR\x06roomId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\"/\n\x14GetBedsByRoomRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\"\x8d\x01\n\x15GetBedsByRoomResponse\x12I\n\x04\x62\x65\x64s\x18\x01 \x03(\x0b\x32\x35.proto.services.task_svc.v1.GetBedsByRoomResponse.BedR\x04\x62\x65\x64s\x1a)\n\x03\x42\x65\x64\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"n\n\x10UpdateBedRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1c\n\x07room_id\x18\x02 \x01(\tH\x00R\x06roomId\x88\x01\x01\x12\x17\n\x04name\x18\x03 \x01(\tH\x01R\x04name\x88\x01\x01\x42\n\n\x08_room_idB\x07\n\x05_name\"\x13\n\x11UpdateBedResponse\"\"\n\x10\x44\x65leteBedRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x13\n\x11\x44\x65leteBedResponse2\x8a\x07\n\nBedService\x12j\n\tCreateBed\x12,.proto.services.task_svc.v1.CreateBedRequest\x1a-.proto.services.task_svc.v1.CreateBedResponse\"\x00\x12y\n\x0e\x42ulkCreateBeds\x12\x31.proto.services.task_svc.v1.BulkCreateBedsRequest\x1a\x32.proto.services.task_svc.v1.BulkCreateBedsResponse\"\x00\x12\x61\n\x06GetBed\x12).proto.services.task_svc.v1.GetBedRequest\x1a*.proto.services.task_svc.v1.GetBedResponse\"\x00\x12|\n\x0fGetBedByPatient\x12\x32.proto.services.task_svc.v1.GetBedByPatientRequest\x1a\x33.proto.services.task_svc.v1.GetBedByPatientResponse\"\x00\x12\x64\n\x07GetBeds\x12*.proto.services.task_svc.v1.GetBedsRequest\x1a+.proto.services.task_svc.v1.GetBedsResponse\"\x00\x12v\n\rGetBedsByRoom\x12\x30.proto.services.task_svc.v1.GetBedsByRoomRequest\x1a\x31.proto.services.task_svc.v1.GetBedsByRoomResponse\"\x00\x12j\n\tUpdateBed\x12,.proto.services.task_svc.v1.UpdateBedRequest\x1a-.proto.services.task_svc.v1.UpdateBedResponse\"\x00\x12j\n\tDeleteBed\x12,.proto.services.task_svc.v1.DeleteBedRequest\x1a-.proto.services.task_svc.v1.DeleteBedResponse\"\x00\x42\xd1\x01\n\x1e\x63om.proto.services.task_svc.v1B\x0b\x42\x65\x64SvcProtoP\x01Z\x1bgen/proto/services/task-svc\xa2\x02\x03PST\xaa\x02\x19Proto.Services.TaskSvc.V1\xca\x02\x19Proto\\Services\\TaskSvc\\V1\xe2\x02%Proto\\Services\\TaskSvc\\V1\\GPBMetadata\xea\x02\x1cProto::Services::TaskSvc::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.services.task_svc.v1.bed_svc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.proto.services.task_svc.v1B\013BedSvcProtoP\001Z\033gen/proto/services/task-svc\242\002\003PST\252\002\031Proto.Services.TaskSvc.V1\312\002\031Proto\\Services\\TaskSvc\\V1\342\002%Proto\\Services\\TaskSvc\\V1\\GPBMetadata\352\002\034Proto::Services::TaskSvc::V1'
  _globals['_CREATEBEDREQUEST']._serialized_start=72
  _globals['_CREATEBEDREQUEST']._serialized_end=135
  _globals['_CREATEBEDRESPONSE']._serialized_start=137
  _globals['_CREATEBEDRESPONSE']._serialized_end=172
  _globals['_BULKCREATEBEDSREQUEST']._serialized_start=174
  _globals['_BULKCREATEBEDSREQUEST']._serialized_end=260
  _globals['_BULKCREATEBEDSRESPONSE']._serialized_start=263
  _globals['_BULKCREATEBEDSRESPONSE']._serialized_end=406
  _globals['_BULKCREATEBEDSRESPONSE_BED']._serialized_start=365
  _globals['_BULKCREATEBEDSRESPONSE_BED']._serialized_end=406
  _globals['_GETBEDREQUEST']._serialized_start=408
  _globals['_GETBEDREQUEST']._serialized_end=439
  _globals['_GETBEDRESPONSE']._serialized_start=441
  _globals['_GETBEDRESPONSE']._serialized_end=518
  _globals['_GETBEDBYPATIENTREQUEST']._serialized_start=520
  _globals['_GETBEDBYPATIENTREQUEST']._serialized_end=575
  _globals['_GETBEDBYPATIENTRESPONSE']._serialized_start=578
  _globals['_GETBEDBYPATIENTRESPONSE']._serialized_end=895
  _globals['_GETBEDBYPATIENTRESPONSE_ROOM']._serialized_start=768
  _globals['_GETBEDBYPATIENTRESPONSE_ROOM']._serialized_end=835
  _globals['_GETBEDBYPATIENTRESPONSE_BED']._serialized_start=365
  _globals['_GETBEDBYPATIENTRESPONSE_BED']._serialized_end=406
  _globals['_GETBEDSREQUEST']._serialized_start=897
  _globals['_GETBEDSREQUEST']._serialized_end=913
  _globals['_GETBEDSRESPONSE']._serialized_start=916
  _globals['_GETBEDSRESPONSE']._serialized_end=1070
  _globals['_GETBEDSRESPONSE_BED']._serialized_start=1004
  _globals['_GETBEDSRESPONSE_BED']._serialized_end=1070
  _globals['_GETBEDSBYROOMREQUEST']._serialized_start=1072
  _globals['_GETBEDSBYROOMREQUEST']._serialized_end=1119
  _globals['_GETBEDSBYROOMRESPONSE']._serialized_start=1122
  _globals['_GETBEDSBYROOMRESPONSE']._serialized_end=1263
  _globals['_GETBEDSBYROOMRESPONSE_BED']._serialized_start=365
  _globals['_GETBEDSBYROOMRESPONSE_BED']._serialized_end=406
  _globals['_UPDATEBEDREQUEST']._serialized_start=1265
  _globals['_UPDATEBEDREQUEST']._serialized_end=1375
  _globals['_UPDATEBEDRESPONSE']._serialized_start=1377
  _globals['_UPDATEBEDRESPONSE']._serialized_end=1396
  _globals['_DELETEBEDREQUEST']._serialized_start=1398
  _globals['_DELETEBEDREQUEST']._serialized_end=1432
  _globals['_DELETEBEDRESPONSE']._serialized_start=1434
  _globals['_DELETEBEDRESPONSE']._serialized_end=1453
  _globals['_BEDSERVICE']._serialized_start=1456
  _globals['_BEDSERVICE']._serialized_end=2362
# @@protoc_insertion_point(module_scope)