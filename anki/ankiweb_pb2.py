# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki/ankiweb.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61nki/ankiweb.proto\x12\x0c\x61nki.ankiweb\"@\n\x13GetAddonInfoRequest\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\r\x12\x11\n\taddon_ids\x18\x02 \x03(\r\"=\n\x14GetAddonInfoResponse\x12%\n\x04info\x18\x01 \x03(\x0b\x32\x17.anki.ankiweb.AddonInfo\"S\n\tAddonInfo\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08modified\x18\x02 \x01(\x03\x12\x13\n\x0bmin_version\x18\x03 \x01(\r\x12\x13\n\x0bmax_version\x18\x04 \x01(\r\"t\n\x15\x43heckForUpdateRequest\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x11\n\tbuildhash\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x12\n\ninstall_id\x18\x04 \x01(\x03\x12\x17\n\x0flast_message_id\x18\x05 \x01(\r\"\x93\x01\n\x16\x43heckForUpdateResponse\x12\x18\n\x0bnew_version\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x0c\x63urrent_time\x18\x02 \x01(\x03\x12\x14\n\x07message\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x17\n\x0flast_message_id\x18\x04 \x01(\rB\x0e\n\x0c_new_versionB\n\n\x08_message2\x10\n\x0e\x41nkiwebService2\xcb\x01\n\x15\x42\x61\x63kendAnkiwebService\x12U\n\x0cGetAddonInfo\x12!.anki.ankiweb.GetAddonInfoRequest\x1a\".anki.ankiweb.GetAddonInfoResponse\x12[\n\x0e\x43heckForUpdate\x12#.anki.ankiweb.CheckForUpdateRequest\x1a$.anki.ankiweb.CheckForUpdateResponseB\x02P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anki.ankiweb_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _GETADDONINFOREQUEST._serialized_start=36
  _GETADDONINFOREQUEST._serialized_end=100
  _GETADDONINFORESPONSE._serialized_start=102
  _GETADDONINFORESPONSE._serialized_end=163
  _ADDONINFO._serialized_start=165
  _ADDONINFO._serialized_end=248
  _CHECKFORUPDATEREQUEST._serialized_start=250
  _CHECKFORUPDATEREQUEST._serialized_end=366
  _CHECKFORUPDATERESPONSE._serialized_start=369
  _CHECKFORUPDATERESPONSE._serialized_end=516
  _ANKIWEBSERVICE._serialized_start=518
  _ANKIWEBSERVICE._serialized_end=534
  _BACKENDANKIWEBSERVICE._serialized_start=537
  _BACKENDANKIWEBSERVICE._serialized_end=740
# @@protoc_insertion_point(module_scope)
