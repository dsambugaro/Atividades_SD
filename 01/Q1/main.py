#!/usr/bin/env python3

import argparse

from server import Server
from client import Client

if __name__ == "__main__":
    # Setup parser
    parser = argparse.ArgumentParser(description='Create a socket server')
    parser.add_argument('type', nargs=1, type=str, choices=('server', 'client'),
                        help='type of process: server or client')
    parser.add_argument('host', nargs='?', type=str,
                        help='server IP (default: localhost)',
                        default='localhost')

    parser.add_argument('--port', '-p', nargs=1, type=int,
                        help='server port (default: 5000)',
                        default='5000')

    args = parser.parse_args()
    # Start server
    if args.type[0] == 'server':
        server = Server(args.host, args.port)
        server.start()
    # Start client
    elif args.type[0] == 'client':
        client = Client(args.host, args.port)
        client.start()
