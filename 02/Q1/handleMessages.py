# Handle Messages

import socket
from threading import Thread

class ReceiveMessages(Thread):
    """Thread to receive messages from peer"""
    def __init__(self, conn, encoding):
        Thread.__init__(self)
        self.conn = conn
        self.encoding = encoding
        self.running = False
    
    def is_running(self):
        """Return True if running or False otherwise"""
        return self.running

    def stop(self):
        """Change running variable to False"""
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            try:
                # Set timeout for wainting messages
                self.conn.settimeout(1)
                # Receive data
                data, addr = self.conn.recvfrom(514)
                # Decode data
                nickname_size = data[0]
                nickname = (data[1:nickname_size+1]).decode(self.encoding)
                msg_size = data[nickname_size]
                msg = (data[nickname_size+1:msg_size]).decode(self.encoding)
                # Show data
                print('{} - {} says:\n\t{}'.format(addr[0], nickname, msg))
            except socket.timeout:
                if not self.running:
                    break
                continue
            # Handle Exceptions
            except KeyboardInterrupt:
                self.stop()
                exit(0)
            except Exception as e:
                print('Exception: {}'.format(e))
                self.stop()
                exit(1)


class SendMessages(Thread):
    """Thread to send messages to peer"""
    def __init__(self, host, port, nickname, conn, encoding):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.nickname = nickname
        self.conn = conn
        self.encoding = encoding
        self.running = False

    def is_running(self):
        """Return True if running or False otherwise"""
        return self.running

    def stop(self):
        """Change running variable to False"""
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            try:
                # Get msg to send
                msg = input()
                # Check for exit command
                if msg.lower() == ':exit':
                    self.stop()
                    continue
                # Encode message
                msg_encoded = msg.encode(self.encoding)
                msg_size = (len(msg_encoded)).to_bytes(1, 'big')
                nickname_encoded = self.nickname.encode(self.encoding)
                nickname_size = (len(nickname_encoded)).to_bytes(1, 'big')
                # Send message
                self.conn.sendto(nickname_size + nickname_encoded + msg_size + msg_encoded,
                                 (self.host, self.port))
            # Handle Exceptions
            except KeyboardInterrupt:
                self.stop()
                exit(0)
            except Exception as e:
                print('Exception: {}'.format(e))
                self.stop()
                exit(1)
