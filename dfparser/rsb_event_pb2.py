# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rsb_event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0frsb_event.proto\x12\x03Rsh\"\xdc\x02\n\x05Point\x12$\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x12.Rsh.Point.Channel\x1a\xac\x02\n\x07\x43hannel\x12\n\n\x02id\x18\x01 \x01(\x04\x12(\n\x06\x62locks\x18\x02 \x03(\x0b\x32\x18.Rsh.Point.Channel.Block\x1a\xea\x01\n\x05\x42lock\x12\x0c\n\x04time\x18\x01 \x01(\x04\x12.\n\x06\x66rames\x18\x02 \x03(\x0b\x32\x1e.Rsh.Point.Channel.Block.Frame\x12/\n\x06\x65vents\x18\x03 \x01(\x0b\x32\x1f.Rsh.Point.Channel.Block.Events\x12\x0e\n\x06length\x18\x04 \x01(\x04\x12\x10\n\x08\x62in_size\x18\x05 \x01(\x04\x1a#\n\x05\x46rame\x12\x0c\n\x04time\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x1a+\n\x06\x45vents\x12\r\n\x05times\x18\x01 \x03(\x04\x12\x12\n\namplitudes\x18\x02 \x03(\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rsb_event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POINT._serialized_start=25
  _POINT._serialized_end=373
  _POINT_CHANNEL._serialized_start=73
  _POINT_CHANNEL._serialized_end=373
  _POINT_CHANNEL_BLOCK._serialized_start=139
  _POINT_CHANNEL_BLOCK._serialized_end=373
  _POINT_CHANNEL_BLOCK_FRAME._serialized_start=293
  _POINT_CHANNEL_BLOCK_FRAME._serialized_end=328
  _POINT_CHANNEL_BLOCK_EVENTS._serialized_start=330
  _POINT_CHANNEL_BLOCK_EVENTS._serialized_end=373
# @@protoc_insertion_point(module_scope)
