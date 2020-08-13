# TCP socket server

import socket
import os
import logging as log
from threading import Thread
from datetime import datetime


class ClientThread(Thread):
    """Handle client requests"""
    def __init__(self, ip, port, conn, encoding, default_dir):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        self.encoding = encoding
        self.default_dir = default_dir

    def stop(self):
        """Stop this thread"""
        self.conn.close()
        self.running = False

    def run(self):
        """Handle client requests"""
        self.running = True
        while self.running:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                log.info('Server received data: %s', data)
                command = data.decode(self.encoding).lower()
                response = None
                # Handle commands
                if command == 'exit':
                    # Thread
                    self.conn.send(data)
                    log.info('Client %s:%s disconected', self.ip, self.port)
                    break
                elif command == 'time':
                    # Get time and set response
                    now = datetime.now()
                    response = now.strftime("%H:%M:%S")
                elif command == 'date':
                    # Get date and set response
                    now = datetime.now()
                    response = now.strftime("%d/%m/%Y")
                elif command == 'files':
                    # Get files list
                    files = [file_name for file_name in os.listdir(self.default_dir)
                             if not file_name.startswith('.') and
                             os.path.isfile(os.path.join(self.default_dir, file_name))]
                    # Send list size
                    self.conn.send((len(files)).to_bytes(4, 'big'))
                    for file_name in files:
                        self.conn.send(file_name.encode(self.encoding))
                elif 'down ' in command:
                    file_name = data.decode(self.encoding)
                    file_name = file_name[file_name.index(' ')+1:]
                    file_path = os.path.join(self.default_dir, file_name)
                    # Check if file don't is hidden and is is a file
                    if not file_name.startswith('.') and os.path.isfile(file_path):
                        file_size = os.path.getsize(file_path)
                        # Send file size
                        self.conn.send((file_size).to_bytes(4, 'big'))
                        # Send file
                        with open(file_path, "rb") as file_name:
                            while (byte := file_name.read(1)):
                                self.conn.send(byte)
                    else:
                        # If file doesn't exist or is invalid, send 0 as file size
                        self.conn.send((0).to_bytes(4, 'big'))

                else:
                    response = 'Command not accepted'
                if response:
                    # Send response to client
                    self.conn.send(response.encode(self.encoding))

            except Exception as e:
                log.error("An exception occurred: %s", e)
                self.conn.close()
                exit(1)


class Server:
    """ TCP socket Server"""
    host = None
    port = None
    tcp = None
    threads = []
    encoding = 'utf-8'
    default_dir = os.getenv('HOME')+'/server'

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._setup_log()
        self._create()

    def _setup_log(self):
        """Configures log format and level"""
        log.basicConfig(format='[ %(levelname)s ] %(message)s', level=log.INFO)

    def _create(self):
        """Creates the TCP socket server"""
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp.bind((self.host, self.port))
        log.info('Server created')

    def start(self):
        """Starts the TCP socket server"""
        self.running = True
        log.info('Server started')
        while self.running:
            try:
                self.tcp.listen()
                (conn, (ip, port)) = self.tcp.accept()
                new_client_thread = ClientThread(
                    ip, port, conn, self.encoding, self.default_dir)
                new_client_thread.start()
                log.info('New client connected - %s:%s', ip, port)
                self.threads.append(new_client_thread)
            except KeyboardInterrupt:
                self.stop()
            except Exception as e:
                log.error("An exception occurred: %s", e)
                self.stop()
                exit(1)

    def stop(self):
        """Stops the TCP socket server"""
        log.info('Stopping server...')
        self.running = False
        self.tcp.close()
        for t in self.threads:
            t.join()
        log.info('Server stoped')
