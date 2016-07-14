
# mitmdump deocder

## Description

A helper script for mitmproxy to decode protobuf serialized requests and responses.
It also parses the GetMapObjects responses into a geojson format file that can be viewed using the 'ui'.  The ui is completely clientside, so it should be hostable with any static file server (I use 'http-server').

## Dependencies

Requires mitmproxy, protobuf, geojson, numpy


## Running

`mitmdump -p 8888 -s decode.py "~d pgorelease.nianticlabs.com"`


## Rebuild python classes

### Linux

```
cd idl; ls -1 *.proto | while read filename; do protoc --python_out ../protocol/ $filename; done
```

### Windows

```
cd idl; ls *.proto | ForEach-Object { Invoke-Expression "protoc --proto_path '$($_.DirectoryName)' --python_out ../protocol/ '$($_.FullName)'" }
```


## Rebuild descriptors

### Windows

```
cd idl; ls *.proto | ForEach-Object { Invoke-Expression "protoc --proto_path '$($_.DirectoryName)' -o ../descriptors/$($_.Name).desc '$($_.FullName)'" }
```
