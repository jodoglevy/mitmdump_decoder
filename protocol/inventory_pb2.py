# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import holoholo_shared_pb2 as holoholo__shared__pb2

from holoholo_shared_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='inventory.proto',
  package='PGo',
  syntax='proto3',
  serialized_pb=_b('\n\x0finventory.proto\x12\x03PGo\x1a\x15holoholo_shared.proto\"Z\n\x11GetInventoryProto\x12\x17\n\x0fTimestampMillis\x18\x01 \x01(\x03\x12,\n\x0cItemBeenSeen\x18\x02 \x03(\x0e\x32\x16.PGo.Holoholo.Rpc.Item\"Y\n\x14GetInventoryOutProto\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x30\n\x0eInventoryDelta\x18\x02 \x01(\x0b\x32\x18.PGo.InventoryDeltaProto\"v\n\x13InventoryDeltaProto\x12\x19\n\x11OriginalTimestamp\x18\x01 \x01(\x03\x12\x14\n\x0cNewTimestamp\x18\x02 \x01(\x03\x12.\n\rInventoryItem\x18\x03 \x03(\x0b\x32\x17.PGo.InventoryItemProto\"U\n\x12InventoryItemProto\x12\x19\n\x11ModifiedTimestamp\x18\x01 \x01(\x03\x12\x16\n\x0e\x44\x65letedItemKey\x18\x02 \x01(\t\x12\x0c\n\x04Item\x18\x03 \x01(\t\"G\n\x10RecycleItemProto\x12$\n\x04Item\x18\x01 \x01(\x0e\x32\x16.PGo.Holoholo.Rpc.Item\x12\r\n\x05\x43ount\x18\x02 \x01(\x05\"\xc4\x01\n\x13RecycleItemOutProto\x12\x33\n\x06Result\x18\x01 \x01(\x0e\x32#.PGo.RecycleItemOutProto.ResultEnum\x12\x10\n\x08NewCount\x18\x02 \x01(\x05\"f\n\nResultEnum\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1b\n\x17\x45RROR_NOT_ENOUGH_COPIES\x10\x02\x12#\n\x1f\x45RROR_CANNOT_RECYCLE_INCUBATORS\x10\x03P\x00\x62\x06proto3')
  ,
  dependencies=[holoholo__shared__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RECYCLEITEMOUTPROTO_RESULTENUM = _descriptor.EnumDescriptor(
  name='ResultEnum',
  full_name='PGo.RecycleItemOutProto.ResultEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_ENOUGH_COPIES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CANNOT_RECYCLE_INCUBATORS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=605,
  serialized_end=707,
)
_sym_db.RegisterEnumDescriptor(_RECYCLEITEMOUTPROTO_RESULTENUM)


_GETINVENTORYPROTO = _descriptor.Descriptor(
  name='GetInventoryProto',
  full_name='PGo.GetInventoryProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TimestampMillis', full_name='PGo.GetInventoryProto.TimestampMillis', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ItemBeenSeen', full_name='PGo.GetInventoryProto.ItemBeenSeen', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=137,
)


_GETINVENTORYOUTPROTO = _descriptor.Descriptor(
  name='GetInventoryOutProto',
  full_name='PGo.GetInventoryOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='PGo.GetInventoryOutProto.Success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InventoryDelta', full_name='PGo.GetInventoryOutProto.InventoryDelta', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=228,
)


_INVENTORYDELTAPROTO = _descriptor.Descriptor(
  name='InventoryDeltaProto',
  full_name='PGo.InventoryDeltaProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='OriginalTimestamp', full_name='PGo.InventoryDeltaProto.OriginalTimestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NewTimestamp', full_name='PGo.InventoryDeltaProto.NewTimestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InventoryItem', full_name='PGo.InventoryDeltaProto.InventoryItem', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=348,
)


_INVENTORYITEMPROTO = _descriptor.Descriptor(
  name='InventoryItemProto',
  full_name='PGo.InventoryItemProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ModifiedTimestamp', full_name='PGo.InventoryItemProto.ModifiedTimestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeletedItemKey', full_name='PGo.InventoryItemProto.DeletedItemKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Item', full_name='PGo.InventoryItemProto.Item', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=435,
)


_RECYCLEITEMPROTO = _descriptor.Descriptor(
  name='RecycleItemProto',
  full_name='PGo.RecycleItemProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Item', full_name='PGo.RecycleItemProto.Item', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Count', full_name='PGo.RecycleItemProto.Count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=508,
)


_RECYCLEITEMOUTPROTO = _descriptor.Descriptor(
  name='RecycleItemOutProto',
  full_name='PGo.RecycleItemOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='PGo.RecycleItemOutProto.Result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NewCount', full_name='PGo.RecycleItemOutProto.NewCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECYCLEITEMOUTPROTO_RESULTENUM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=707,
)

_GETINVENTORYPROTO.fields_by_name['ItemBeenSeen'].enum_type = holoholo__shared__pb2._HOLOHOLO_RPC_ITEM
_GETINVENTORYOUTPROTO.fields_by_name['InventoryDelta'].message_type = _INVENTORYDELTAPROTO
_INVENTORYDELTAPROTO.fields_by_name['InventoryItem'].message_type = _INVENTORYITEMPROTO
_RECYCLEITEMPROTO.fields_by_name['Item'].enum_type = holoholo__shared__pb2._HOLOHOLO_RPC_ITEM
_RECYCLEITEMOUTPROTO.fields_by_name['Result'].enum_type = _RECYCLEITEMOUTPROTO_RESULTENUM
_RECYCLEITEMOUTPROTO_RESULTENUM.containing_type = _RECYCLEITEMOUTPROTO
DESCRIPTOR.message_types_by_name['GetInventoryProto'] = _GETINVENTORYPROTO
DESCRIPTOR.message_types_by_name['GetInventoryOutProto'] = _GETINVENTORYOUTPROTO
DESCRIPTOR.message_types_by_name['InventoryDeltaProto'] = _INVENTORYDELTAPROTO
DESCRIPTOR.message_types_by_name['InventoryItemProto'] = _INVENTORYITEMPROTO
DESCRIPTOR.message_types_by_name['RecycleItemProto'] = _RECYCLEITEMPROTO
DESCRIPTOR.message_types_by_name['RecycleItemOutProto'] = _RECYCLEITEMOUTPROTO

GetInventoryProto = _reflection.GeneratedProtocolMessageType('GetInventoryProto', (_message.Message,), dict(
  DESCRIPTOR = _GETINVENTORYPROTO,
  __module__ = 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GetInventoryProto)
  ))
_sym_db.RegisterMessage(GetInventoryProto)

GetInventoryOutProto = _reflection.GeneratedProtocolMessageType('GetInventoryOutProto', (_message.Message,), dict(
  DESCRIPTOR = _GETINVENTORYOUTPROTO,
  __module__ = 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GetInventoryOutProto)
  ))
_sym_db.RegisterMessage(GetInventoryOutProto)

InventoryDeltaProto = _reflection.GeneratedProtocolMessageType('InventoryDeltaProto', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYDELTAPROTO,
  __module__ = 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:PGo.InventoryDeltaProto)
  ))
_sym_db.RegisterMessage(InventoryDeltaProto)

InventoryItemProto = _reflection.GeneratedProtocolMessageType('InventoryItemProto', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYITEMPROTO,
  __module__ = 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:PGo.InventoryItemProto)
  ))
_sym_db.RegisterMessage(InventoryItemProto)

RecycleItemProto = _reflection.GeneratedProtocolMessageType('RecycleItemProto', (_message.Message,), dict(
  DESCRIPTOR = _RECYCLEITEMPROTO,
  __module__ = 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:PGo.RecycleItemProto)
  ))
_sym_db.RegisterMessage(RecycleItemProto)

RecycleItemOutProto = _reflection.GeneratedProtocolMessageType('RecycleItemOutProto', (_message.Message,), dict(
  DESCRIPTOR = _RECYCLEITEMOUTPROTO,
  __module__ = 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:PGo.RecycleItemOutProto)
  ))
_sym_db.RegisterMessage(RecycleItemOutProto)


# @@protoc_insertion_point(module_scope)
