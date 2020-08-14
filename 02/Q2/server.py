# UDP socket server

import socket
import os
import hashlib
import logging as log


class Server:
    """ UDP socket File Server"""
    host = None
    port = None
    conn = None
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
        """Creates the UDP socket server"""
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.conn.bind((self.host, self.port))
        log.info('Server created')

    def start(self):
        """Starts the UDP socket file server"""
        self.running = True
        log.info('Server started')
        while self.running:
            try:
                self.conn.settimeout(5)
                data, addr = self.conn.recvfrom(260)
                # Decode data from header
                file_name_size = data[0]
                file_name = (data[1:file_name_size+1]).decode(self.encoding)
                file_size = int.from_bytes(data[file_name_size+1:], 'big')
                log.info('Receiving file {} ({} bytes) from client {}'.format(
                    file_name, file_size, addr))
                # Get file path
                file_path = os.path.join(
                    self.default_dir, file_name)
                count_file_size = file_size
                # Get file bytes in memory
                file_data = {}
                while count_file_size:
                    data_aux, addr = self.conn.recvfrom(1025)
                    file_data[data_aux[0]] = data_aux[1:]
                    count_file_size -= len(data_aux[1:])
                # Get MD5 from client
                data_md5, addr = self.conn.recvfrom(256)
                md5_size = data_md5[0]
                md5_check = data_md5[1:]
                log.info('File {} received'.format(file_name))
                log.info('MD5 to file {} received: {}'.format(
                    file_name, md5_check))
                keys = list(file_data.keys())
                keys.sort()
                # Get MD5 from bytes received
                hasher = hashlib.md5()
                file_bytes = b''
                for key in keys:
                    file_bytes += file_data[key]
                hasher.update(file_bytes)
                md5_obteined = hasher.digest()
                log.info('MD5 to file {} obtained: {}'.format(
                    file_name, md5_obteined))
                # Check MD5
                if md5_check == md5_obteined:
                    log.info('Checksum match! Saving file')
                    # Save file
                    with open(file_path, "wb") as afile:
                        afile.write(file_bytes)
                    log.info('File saved in 1{}'.format(file_path))
                else:
                    log.error('Checksum md5 to file {} from client {} doesn\'t match'.format(
                        file_name, addr))
            # Handle exceptions
            except socket.timeout:
                continue
            except KeyboardInterrupt:
                self.stop()
            except Exception as e:
                log.error("An exception occurred: %s", e)
                self.stop()
                exit(1)

    def stop(self):
        """Stops the UDP socket file server"""
        log.info('Stopping server...')
        self.running = False
        log.info('Server stoped')
