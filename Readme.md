
Requires mitmproxy, protobuf

$ mitmdump -p 8888 -s decode.py "~d pgorelease.nianticlabs.com"

## Rebuild python classes

cd idl; ls -1 *.proto | while read filename; do protoc --python_out ../protocol/ $filename; done
