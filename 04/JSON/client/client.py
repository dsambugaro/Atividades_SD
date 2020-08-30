# TCP socket client

import socket
import os
import logging as log

from response import Response
from request import Request


class Client:
    """ TCP socket Client"""
    host = None
    port = None
    conn = None
    connected = False
    threads = []
    encoding = 'utf-8'
    default_dir = os.getenv('HOME')+'/client'

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
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.host, self.port))
        self.connected = True
        log.info('Client connected to %s:%s', self.host, self.port)

    def show_help(self):
        """Prints commands list on console"""
        print('* * * * * * * * * * * * * MENU * * * * * * * * * * * * *')
        print('DEFINE_NOTA <cod. disciplina> <RA> <ano/semestre> <nota>\n\tDefine a nota do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('REMOVE_NOTA <cod. disciplina> <RA> <ano/semestre>\n\tRemove a nota do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('DEFINE_FALTA <cod. disciplina> <RA> <ano/semestre> <faltas>\n\tDefine as faltas do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('REMOVE_FALTA <cod. disciplina> <RA> <ano/semestre>\n\tRemove as faltas do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('LISTAR_ALUNOS <cod. disciplina> <ano/semestre>\n\tLista os alunos numa dada disciplina num dado semestre e ano letivo\n')
        print('AJUDA\n\tMostra esse texto\n')
        print('SAIR\n\tFecha o cliente\n')
        print('* * * * * * * * * * * * * *  * * * * * * * * * * * * * *')

    def new_request(self, action, target, course_code, academic_semester,
                    academic_year, academic_code, value):
        """Creates a new request from args"""
        request = Request()
        request.action = action if action else 0 # default: 0
        request.target = target if target else '' # default: ''
        request.course_code = course_code if course_code else '' # default: ''
        request.academic_semester = academic_semester if academic_year else 0 # default: 0
        request.academic_year = academic_year if academic_year else 0 # default: 0
        request.academic_code = academic_code if academic_code else 0 # default: 0
        request.value = value if value else 0.0 # default: 0.0
        return request

    def new_response(self, reponse_bytes):
        """Creates a new response from bytes"""
        # Decodes json from bytes and create new Response
        return Response.from_json(reponse_bytes.decode('utf-8'))

    def start(self):
        """Interacts with server"""
        log.info('Client started')
        if not self.connected:
            log.error('Client not connected')
            exit(1)

        # Prints menu
        self.show_help()

        while True:
            command = input('Comando: ')
            args = command.split(' ') # Split args from input
            if 'sair' == args[0].lower():
                break # Exit client
            elif 'listar_alunos' in args[0].lower():
                semester_year = args[2].split('/') # Get semester and year
                # Create a new request
                request = self.new_request(
                    3, 'alunos', args[1], int(semester_year[0]),
                    int(semester_year[1]), None, None)
                # Get request in json format
                request_json = request.to_json()
                # Get json bytes and send to server
                self.conn.send(request_json.encode('utf-8'))
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                elif len(response.data):
                    # Print results
                    for student in response.data:
                        print('{} - {}'.format(student['ra'],
                                               student['nome']))
                else:
                    # Print this msg if no results are found
                    print('Sem resultados')
                print('===================================\n')
            elif 'define_nota' in args[0].lower():
                semester_year = args[3].split('/') # Get semester and year
                # Create a new request
                request = self.new_request(
                    1, 'grade', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), float(args[4]))
                # Get request in json format
                request_json = request.to_json()
                # Get json bytes and send to server
                self.conn.send(request_json.encode('utf-8'))
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Nota definida com sucesso')
                print('===================================\n')
            elif 'remove_nota' in args[0].lower():
                semester_year = args[3].split('/') # Get semester and year
                # Create a new request
                request = self.new_request(
                    2, 'grade', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), None)
                # Get request in json format
                request_json = request.to_json()
                # Get json bytes and send to server
                self.conn.send(request_json.encode('utf-8'))
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Nota removida com sucesso')
                print('===================================\n')
            elif 'define_falta' in args[0].lower():
                semester_year = args[3].split('/') # Get semester and year
                # Create a new request
                request = self.new_request(
                    1, 'absences', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), float(args[4]))
                # Get request in json format
                request_json = request.to_json()
                # Get json bytes and send to server
                self.conn.send(request_json.encode('utf-8'))
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Faltas definida com sucesso')
                print('===================================\n')
            elif 'remove_falta' in args[0].lower():
                semester_year = args[3].split('/') # Get semester and year
                # Create a new request
                request = self.new_request(
                    2, 'absences', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), None)
                # Get request in json format
                request_json = request.to_json()
                # Get json bytes and send to server
                self.conn.send(request_json.encode('utf-8'))
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Faltas removidas com sucesso')
                print('===================================\n')
            else:
                # Command invalid
                print('\nComando inválido\n')
