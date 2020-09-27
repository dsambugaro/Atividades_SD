#!/usr/bin/env python3

import argparse

from client import Client

if __name__ == "__main__":
    # Setup parser
    parser = argparse.ArgumentParser(description='Create a socket client')
    parser.add_argument('host', nargs='?', type=str,
                        help='server IP (default: localhost)',
                        default='127.0.0.1')

    parser.add_argument('--port', '-p', nargs=1, type=int,
                        help='server port (default: 5000)',
                        default=[5000])

    args = parser.parse_args()
    client = Client(args.host, args.port[0])
    client.start()
