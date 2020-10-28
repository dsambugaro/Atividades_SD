# TCP socket client

import socket
import os
import logging as log


class Client:
    """ TCP socket Client"""
    host = None
    port = None
    tcp = None
    connected = False
    threads = []
    encoding = 'utf-8'
    default_dir = os.getenv('HOME')+os.path.sep+'client'

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._setup_log()
        self._connect()

    def _setup_log(self):
        """Configures log format and level"""
        log.basicConfig(format='[ %(levelname)s ] %(message)s', level=log.INFO)

    def _connect(self):
        """Connects to a TCP socket server"""
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.connect((self.host, self.port))
        self.connected = True
        log.info('Client connected to %s:%s', self.host, self.port)

    def start(self):
        log.info('Client started')
        if not self.connected:
            log.error('Client not connected')
            exit(1)

        while True:
            command = input('Command: ')
            self.tcp.send(command.encode(self.encoding))
            data = self.tcp.recv(1024)
            response = data.decode(self.encoding).lower()
            if response == 'exit':
                break
            elif command.lower() == 'files':
                files_number = int.from_bytes(data, 'big')
                if not files_number:
                    print('No files found')
                else:
                    print('{} file(s) found:'.format(files_number))
                    while files_number:
                        file_name = self.tcp.recv(1024)
                        print(file_name.decode(self.encoding))
                        files_number -= 1
            elif 'down ' in command.lower():
                file_size = int.from_bytes(data, 'big')
                if not file_size:
                    print('File not found')
                else:
                    file_name = command[command.index(' ')+1:]
                    file_path = os.path.join(self.default_dir, file_name)
                    print('Downloading file {}...'.format(file_name))
                    with open(file_path, "wb") as f:
                        while file_size:
                            f.write(self.tcp.recv(1))
                            file_size -= 1
                    print('File {} downloaded'.format(file_name))
            else:
                print('Response: ', response)
