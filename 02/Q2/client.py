# UDP socket client

import socket
import os
import hashlib
import logging as log


class Client:
    """ UDP socket Client"""
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

    def _setup_log(self):
        """Configures log format and level"""
        log.basicConfig(format='[ %(levelname)s ] %(message)s', level=log.INFO)

    def start(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        log.info('Client started')
        print('\n\t\tServer: {}:{}\n\t\tSend files to server!\n\t\tType "exit" to exit\n'.format(
            self.host, self.port))
        while True:
            command = input('File path: ')
            if command.lower() == 'exit':
                break
            else:
                file_path = command
                if not os.path.exists(file_path):
                    log.error('File %s not found', file_path)
                # Check if file path is a file
                elif not os.path.isfile(file_path):
                    log.error('%s is not a valid file', file_path)
                else:
                    # Get file name
                    file_name = file_path[file_path.rfind(
                        os.path.sep)+1:].encode(self.encoding)
                    # Get file name size
                    file_name_size = (len(file_name)).to_bytes(1, 'big')
                    # Get file size
                    file_size = (os.path.getsize(file_path)).to_bytes(4, 'big')
                    # Send header to server
                    self.conn.sendto(file_name_size + file_name +
                                     file_size, (self.host, self.port))
                    # Send file to server
                    chunk = 1
                    hasher = hashlib.md5()
                    with open(file_path, "rb") as f:
                        while (file_bytes := f.read(1024)):
                            # Update hash to get md5
                            hasher.update(file_bytes)
                            self.conn.sendto(chunk.to_bytes(
                                1, 'big') + file_bytes, (self.host, self.port))
                            chunk += 1
                    # Get md5
                    md5_bytes = hasher.digest()
                    # Get md5 size
                    md5_size = (len(md5_bytes)).to_bytes(1, 'big')
                    # Send MD5 to server
                    self.conn.sendto((md5_size + md5_bytes),
                                     (self.host, self.port))
