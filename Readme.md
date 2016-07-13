
Requires mitmproxy, protobuf

$ mitmdump -p 8888 -s decode.py "~d pgorelease.nianticlabs.com"


## Rebuild python classes

### Linux

cd idl; ls -1 *.proto | while read filename; do protoc --python_out ../protocol/ $filename; done

### Windows

cd idl; ls *.proto | ForEach-Object { Invoke-Expression "protoc --proto_path '$($_.DirectoryName)' --python_out ../protocol/ '$($_.FullName)'" }


## Rebuild descriptors

### Windows

cd idl; ls *.proto | ForEach-Object { Invoke-Expression "protoc --proto_path '$($_.DirectoryName)' -o ../descriptors/$($_.Name).desc '$($_.FullName)'" }