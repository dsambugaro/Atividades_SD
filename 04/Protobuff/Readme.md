
Dependencies:
- Python 3.x
- Node.js 12.x.x
- protoc 3.13.x

Compile protobuf file for server - run:

```bash
$ protoc --js_out=import_style=commonjs,binary:server protobuf_model.proto
```

Compile protobuf file for client - run:

```bash
$ protoc --python_out=client protobuf_model.proto
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