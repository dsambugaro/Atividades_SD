#!/usr/bin/env python3

import argparse

from chat import Chat

if __name__ == "__main__":
    # Setup parser
    parser = argparse.ArgumentParser(description='Create a P2P chat using UDP')
    
    parser.add_argument('port', nargs=1, type=int,
                        help='Your UDP port')
    
    parser.add_argument('nickname', nargs=1, type=str,
                        help='Your nickname on chat')
    
    parser.add_argument('peer_ip', nargs=1, type=str,
                        help='Peer IP')
    
    parser.add_argument('peer_port', nargs=1, type=int,
                        help='Peer UDP port')

    args = parser.parse_args()
    # Start chat
    chat = Chat(args.peer_ip[0], args.peer_port[0], args.nickname[0], args.port[0])
    chat.start()
