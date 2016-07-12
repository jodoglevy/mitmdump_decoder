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

@concurrent  # Remove this and see what happens
def request(context, flow):
  if flow.match("~d pgorelease.nianticlabs.com"):
    print("handle request: %s%s" % (flow.request.host, flow.request.path))
    env = RpcRequestEnvelopeProto()
    env.ParseFromString(flow.request.content)
    key = env.parameter[0].key
    value = env.parameter[0].value

    if (key == GET_MAP_OBJECTS):
      mor = MapObjectsRequest()
      mor.ParseFromString(value)
      print(mor)
    elif (key == FORT_DETAILS):
      pass
    else:
      print("API: %s" % key)
