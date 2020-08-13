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
        self.running = False

    def stop(self):
        """Stop this thread"""
        self.conn.close()
        self.running = False

    def run(self):
        """Handle client requests"""
        self.running = True
        while self.running:
            try:
                # receive data from client
                data = self.conn.recv(260)
                if not data:
                    log.info('Client %s disconected', self.ip)
                    break
                log.info('Received data: {} from client {}'.format(data, self.ip))
                log.info('Decoding data')
                msg_type = data[0]
                # If msg is of type request (1)
                if msg_type == 1:
                    command_type = data[1]
                    file_name_size = data[2]
                    if file_name_size:
                        file_name = (data[3:3+file_name_size]
                                     ).decode(self.encoding)
                    # Change message type to responde (2)
                    msg_type = (2).to_bytes(1, 'big')
                    status = (1).to_bytes(1, 'big')
                    try:
                        # Handle commands
                        if command_type == 1:
                            log.info(
                                'Command ADDFILE received from client %s', self.ip)
                            # Get new file size
                            file_size = int.from_bytes(
                                self.conn.recv(4), 'big')
                            # Get new file path
                            file_path = os.path.join(
                                self.default_dir, file_name)
                            # Get write new file
                            with open(file_path, "wb") as file:
                                while file_size:
                                    file.write(self.conn.recv(1))
                                    file_size -= 1
                            log.info('Added file {} from client {}'.format(
                                file_name, self.ip))
                            # Send response to client
                            self.conn.sendall(msg_type + command_type.to_bytes(1, 'big') + status)
                        elif command_type == 4:
                            # Get file path
                            file_path = os.path.join(
                                self.default_dir, file_name)
                            log.info(
                                'Command GETFILE received from client %s', self.ip)
                            # Check if path existis
                            if not os.path.exists(file_path):
                                log.error('File %s not found', file_path)
                                raise Exception(
                                    'File {} not found'.format(file_path))
                            # Check if path is a file
                            elif not os.path.isfile(file_path):
                                log.error('%s is not a valid file', file_path)
                                raise Exception(
                                    '{} is not a valid file'.format(file_path))
                            else:
                                # Get file size
                                file_size = (os.path.getsize(
                                    file_path)).to_bytes(4, 'big')
                                # Send response to client with file size
                                self.conn.sendall(
                                    msg_type + command_type.to_bytes(1, 'big') + status + file_size)
                                log.info('Sending file {} to client {}'.format(
                                    file_name, self.ip))
                                # Send file to client
                                with open(file_path, "rb") as f:
                                    while (byte := f.read(1)):
                                        self.conn.sendall(byte)
                                log.info('File {} sended to client {}'.format(
                                    file_name, self.ip))
                        elif command_type == 2:
                            # Send file path to delete
                            file_path = os.path.join(
                                self.default_dir, file_name)
                            log.info(
                                'Command DELETE received from client %s', self.ip)
                            # Check if path existis
                            if not os.path.exists(file_path):
                                log.error('File %s not found', file_path)
                                raise Exception(
                                    'File {} not found'.format(file_path))
                            # Check if path is a file
                            elif not os.path.isfile(file_path):
                                log.error('%s is not a valid file', file_path)
                                raise Exception(
                                    '{} is not a valid file'.format(file_path))
                            else:
                                # Remove file from server
                                os.remove(file_path)
                                log.info('Client {} deleted file {}'.format(
                                    self.ip, file_name))
                                # Send response to client
                                self.conn.sendall(
                                    msg_type + command_type.to_bytes(1, 'big') + status)
                        elif command_type == 3:
                            # Get files list
                            files = [f for f in os.listdir(self.default_dir)
                                     if not f.startswith('.') and
                                     os.path.isfile(os.path.join(self.default_dir, f))]
                            qt_files = (len(files)).to_bytes(2, 'big')
                            # Send response to client with files list size
                            self.conn.sendall(
                                msg_type + command_type.to_bytes(1, 'big') + status + qt_files)
                            for file_name in files:
                                # Get file name size
                                file_name_size = (
                                    len(file_name)).to_bytes(1, 'big')
                                # Sent file name size and file name to client
                                self.conn.sendall(
                                    file_name_size + file_name.encode(self.encoding))
                    except Exception:
                        # Send error response to client
                        status = (2).to_bytes(1, 'big')
                        self.conn.sendall(msg_type + command_type.to_bytes(1, 'big') + status)
            except Exception as e:
                log.error("An exception occurred: %s", e)
                self.stop()
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
        """Configures log file, format and level"""
        log.basicConfig(filename=os.path.join(self.default_dir, '.server.log'),
                        format='[%(asctime)s - %(levelname)s ] %(message)s', level=log.INFO)

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
                # Start listen
                self.tcp.listen()
                (conn, (ip, port)) = self.tcp.accept()
                new_client_thread = ClientThread(
                    ip, port, conn, self.encoding, self.default_dir)
                new_client_thread.start()
                log.info('New client connected - %s:%s', ip, port)
                # Create new thread to handle client
                self.threads.append(new_client_thread)
            except KeyboardInterrupt:
                # On KeyboardInterrupt stops server
                self.stop()
            except Exception as e:
                log.error("An exception occurred: %s", e)
                # On Exception stops server
                self.stop()
                exit(1)

    def stop(self):
        """Stops the TCP socket server"""
        log.info('Stopping server...')
        self.running = False
        # Close server
        self.tcp.close()
        # Wait for clients desconnect
        for thread in self.threads:
            thread.stop()
            thread.join()
        log.info('Server stoped')