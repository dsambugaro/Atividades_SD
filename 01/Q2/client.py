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

    def show_help(self):
        """Prints commands list on console"""
        print('* * * * * * * * * * * * * MENU * * * * * * * * * * * * *')
        print('ADDFILE <file_path>\tAdds a file to server')
        print('DELETE <file_name>\tDeletes a file from server')
        print('GETFILESLIST\t\tGet file list from server')
        print('GETFILE <file_name>\tDownloads a file from server')
        print('HELP\t\t\tShow this text')
        print('EXIT\t\t\tCloses the aplication')
        print('* * * * * * * * * * * * * *  * * * * * * * * * * * * * *')

    def start(self):
        """Interacts with server"""
        log.info('Client started')
        if not self.connected:
            log.error('Client not connected')
            exit(1)

        self.show_help()

        while True:
            msg_type = (1).to_bytes(1, 'big')
            command_type = (0).to_bytes(1, 'big')
            file_name = ''.encode(self.encoding)
            file_name_size = (len(file_name)).to_bytes(1, 'big')
            command = input('Command: ')
            if 'exit' in command.lower():
                break
            elif 'help' in command.lower():
                self.show_help()
            elif 'addfile ' in command.lower():
                command_type = (1).to_bytes(1, 'big')
                # Get file path
                file_path = command[command.index(' ')+1:]
                # Check if file path exists
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
                    # Send request to server
                    self.tcp.sendall(msg_type + command_type +
                                     file_name_size + file_name)
                    file_size = os.path.getsize(file_path)
                    # Send file size to server
                    self.tcp.sendall(file_size.to_bytes(4, 'big'))
                    print('Uploading file...')
                    # Send file to server
                    with open(file_path, "rb") as f:
                        while (byte := f.read(1)):
                            self.tcp.sendall(byte)
                    # Handle response from server
                    response = self.tcp.recv(3)
                    # Success
                    if response[2] == 1:
                        print('File uploaded')
                    # Error
                    elif response[2] == 2:
                        print('Error while uploading file to server')
                    else:
                        print('Unknow error')
            elif 'getfile ' in command.lower():
                command_type = (4).to_bytes(1, 'big')
                file_name = command[command.index(' ')+1:]
                file_name_size = (len(file_name)).to_bytes(1, 'big')
                # Send request to server
                self.tcp.sendall(msg_type + command_type +
                                 file_name_size + file_name.encode(self.encoding))
                # Handle response from server
                response = self.tcp.recv(7)
                # Error
                if response[2] == 2:
                    print('Error while downloading file from server')
                # Success
                elif response[2] == 1:
                    # Get file size
                    file_size = int.from_bytes(response[3:7], 'big')
                    # Get file path
                    file_path = os.path.join(self.default_dir, file_name)
                    print('Downloading file {}'.format(file_name))
                    # Get file from server
                    with open(file_path, "wb") as file:
                        while file_size:
                            file.write(self.tcp.recv(1))
                            file_size -= 1
                    print('File {} downloaded'.format(file_name))
            elif 'getfileslist' in command.lower():
                command_type = (3).to_bytes(1, 'big')
                # Send request to server
                self.tcp.sendall(msg_type + command_type +
                                 file_name_size + file_name)
                # Handle response from server
                response = self.tcp.recv(5)
                # Error
                if response[2] == 2:
                    print('Error while downloading file from server')
                # Success
                elif response[2] == 1:
                    # Get list size
                    list_size = int.from_bytes(response[3:5], 'big')
                    # Get files names
                    while list_size:
                        data = self.tcp.recv(256)
                        file_name_size = data[0]
                        file_name = (data[1:file_name_size+1]
                                     ).decode(self.encoding)
                        print(file_name)
                        list_size -= 1
            elif 'delete' in command.lower():
                command_type = (2).to_bytes(1, 'big')
                file_name = command[command.index(' ')+1:]
                file_name_size = (len(file_name)).to_bytes(1, 'big')
                # Send request to server
                self.tcp.sendall(msg_type + command_type +
                                 file_name_size + file_name.encode(self.encoding))
                # Handle response from server
                response = self.tcp.recv(3)
                # Error
                if response[2] == 2:
                    print('Error while deleting file from server')
                # Success
                elif response[2] == 1:
                    print('File deleted')
            else:
                print('Command not accepted')
