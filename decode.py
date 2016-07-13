#!/usr/bin/env python

import time
import sys
from mitmproxy.script import concurrent
from mitmproxy.models import decoded


import site
site.addsitedir("/usr/local/Cellar/protobuf/3.0.0-beta-3/libexec/lib/python2.7/site-packages")
sys.path.append("/usr/local/lib/python2.7/site-packages")
sys.path.append("/usr/local/Cellar/protobuf/3.0.0-beta-3/libexec/lib/python2.7/site-packages")
from google.protobuf.internal import enum_type_wrapper

from envelope_pb2 import *
from get_map_objects_pb2 import *

associate = {} #Match responses to their requests

@concurrent  # Remove this and see what happens
def request(context, flow):
  if flow.match("~d pgorelease.nianticlabs.com"):
    env = RpcRequestEnvelopeProto()
    env.ParseFromString(flow.request.content)
    key = env.parameter[0].key
    value = env.parameter[0].value

    associate[env.request_id] = key

    if (key == GET_MAP_OBJECTS):
      mor = MapObjectsRequest()
      mor.ParseFromString(value)
      print(mor)
    else:
      print("API: %s" % key)

def response(context, flow):
  with decoded(flow.response):
    if flow.match("~d pgorelease.nianticlabs.com"):
      env = RpcResponseEnvelopeProto()
      env.ParseFromString(flow.response.content)
      key = associate[env.response_id]
      value = env.returns[0]

      if (key == GET_MAP_OBJECTS):
        mor = MapObjectsResponse()
        mor.ParseFromString(value)
        print("GET_MAP_OBJECTS %i tiles", len(mor.tiles))
        for tile in mor.tiles:
          print("%i forts(3) | %i forts(4) | %i forts(5) | %i forts(9)" % (len(tile.forts3), len(tile.forts4), len(tile.forts5), len(tile.forts9)))
          for fort in tile.forts3:
            print("%s: %f, %f" % (fort.id, fort.lat, fort.long))
      else:
        print("API: %s" % key)


