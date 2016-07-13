#!/usr/bin/env python

import time
import sys
from mitmproxy.script import concurrent
from mitmproxy.models import decoded

from geojson import GeometryCollection, Point, Feature, FeatureCollection
import geojson

import site
site.addsitedir("/usr/local/Cellar/protobuf/3.0.0-beta-3/libexec/lib/python2.7/site-packages")
sys.path.append("/usr/local/lib/python2.7/site-packages")
sys.path.append("/usr/local/Cellar/protobuf/3.0.0-beta-3/libexec/lib/python2.7/site-packages")
from google.protobuf.internal import enum_type_wrapper

from protocol.map_pb2 import *
from protocol.rpc_pb2 import *
from protocol.fortdetails_pb2 import *

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
    elif (key == FORT_DETAILS):
      mor = FortDetailsProto()
      mor.ParseFromString(value)
      print(mor)
    elif (key == FORT_SEARCH):
      mor = FortSearchProto()
      mor.ParseFromString(value)
      print(mor)
    elif (key == GET_GYM_DETAILS):
      mor = FortDetailsProto()
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
        print("GET_MAP_OBJECTS %i tiles" % len(mor.tiles))
        features = []

        for tile in mor.tiles:
          print("S2 Cell %i" % tile.id)
          for fort in tile.forts:
            p = Point((fort.longitude, fort.latitude))
            f = Feature(geometry=p, id=len(features), properties={"id": fort.id, "tile": tile.id, "type": "fort", "marker-color": "0000FF"})
            features.append(f)

          for fort in tile.location4:
            p = Point((fort.longitude, fort.latitude))
            f = Feature(geometry=p, id=len(features), properties={"tile": tile.id, "type": "location4", "marker-color": "FFFF00"})
            features.append(f)

          for fort in tile.location9:
            p = Point((fort.longitude, fort.latitude))
            f = Feature(geometry=p, id=len(features), properties={"tile": tile.id, "type": "location9", "marker-color": "00FFFF"})
            features.append(f)

          for fort in tile.close_pokemon_a:
            p = Point((fort.longitude, fort.latitude))
            f = Feature(geometry=p, id=len(features), properties={"id": fort.uid, "tile": tile.id, "type": "close_pokemon_a", "marker-color": "FF0000"})
            features.append(f)

          for fort in tile.close_pokemon_b:
            p = Point((fort.longitude, fort.latitude))
            f = Feature(geometry=p, id=len(features), properties={"id": fort.uid, "tile": tile.id, "type": "close_pokemon_b", "marker-color": "00FF00"})
            features.append(f)

        fc = FeatureCollection(features)
        dump = geojson.dumps(fc, sort_keys=True)
        f = open('get_map_objects.json', 'w')
        f.write(dump)
      elif (key == FORT_DETAILS):
        mor = FortDetailsOutProto()
        mor.ParseFromString(value)
        print(mor)
      elif (key == FORT_SEARCH):
        mor = FortSearchOutProto()
        mor.ParseFromString(value)
        print(mor)
      else:
        print("API: %s" % key)


