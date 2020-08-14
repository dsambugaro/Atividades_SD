# P2P UDP chat

import socket
from time import sleep

from handleMessages import SendMessages, ReceiveMessages

class Chat:
    """Chat P2P - Server and client at same time"""
    def __init__(self, peer_host, peer_port, nickname, server_port):
        self.peer_host = peer_host
        self.peer_port = peer_port
        self.nickname = nickname
        self.server = None
        self.client = None
        self.server_port = server_port
        self.encoding = 'utf-8'
        self.threads = []

    def busy_waiting(self):
        try:
            # Busy-waiting - Not the best method
            while (self.receive_thread.is_running() and self.send_thread.is_running()):
                continue
        except KeyboardInterrupt:
            # Handle Interruption by keyboard
            print("Type ':exit' to exit the chat")
            self.busy_waiting()

    def start(self):
        try:
            # Create server socket and bind his port in localhost
            self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.server.bind(('', self.server_port))
            
            # Create server socket
            self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Create thread to send messages with client socket
            self.send_thread = SendMessages(
                self.peer_host, self.peer_port, self.nickname, self.client, self.encoding)
            
            # Create thread to receive messages with server socket
            self.receive_thread = ReceiveMessages(self.server, self.encoding)
            
            # Start Threads
            self.receive_thread.start()
            self.send_thread.start()
                
            print('\tChat started\n\tWelcome {}!'.format(self.nickname))
            print("\tType ':exit' to exit chat")            
 
            # Busy-waiting
            self.busy_waiting()

            # Stop threads
            self.receive_thread.stop()
            self.send_thread.stop()
            
            # Wait for Threads
            self.receive_thread.join()
            self.send_thread.join()
        # Handle Exception
        except Exception as e:
            print('Exception: {}'.format(e))
            exit(1)
