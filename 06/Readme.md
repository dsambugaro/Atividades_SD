
Dependencies:
- Python 3.x
- Node.js 12.x.x
- protoc 3.13.x

Compile protobuf file for server - run:

```bash
$ npm install -g grpc-tools
$ grpc_tools_node_protoc --js_out=import_style=commonjs,binary:server --grpc_out=server/ --plugin=protoc-gen-grpc=`which grpc_tools_node_protoc_plugin` gRPC_model.proto
```

Compile protobuf file for client - run:

```bash
$ pip install grpcio-tools
$ python -m grpc_tools.protoc -I. --python_out=client --grpc_python_out=client gRPC_model.proto
```

Install server depencencies - on server folder run:

```bash
$ npm install
```

Install client depencencies - on client folder run:

```bash
$ pip install -r requirements.txt
```

Start server - on server folder run:
> By default server starts at 127.0.0.1:5000
```bash
$ npm start
```

Start client - on client folder run:
> By default client connects to 127.0.0.1:5000
```bash
$ python main.py
```