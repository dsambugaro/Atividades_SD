# TCP socket client

import socket
import os
import logging as log

from protobuf_model_pb2 import Request, Response


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
        request = Request()
        request.action = action if action else 0
        request.target = target if target else ''
        request.course_code = course_code if course_code else ''
        request.academic_semester = academic_semester if academic_year else 0
        request.academic_year = academic_year if academic_year else 0
        request.academic_code = academic_code if academic_code else 0
        request.value = value if value else 0.0
        return request

    def new_response(self, reponse_bytes):
        response = Response()
        response.ParseFromString(reponse_bytes)
        return response

    def start(self):
        """Interacts with server"""
        log.info('Client started')
        if not self.connected:
            log.error('Client not connected')
            exit(1)

        self.show_help()

        while True:
            command = input('Comando: ')
            args = command.split(' ')
            if 'sair' == args[0].lower():
                break
            elif 'listar_alunos' in args[0].lower():
                semester_year = args[2].split('/')
                request = self.new_request(
                    3, 'alunos', args[1], int(semester_year[0]),
                    int(semester_year[1]), None, None)
                self.conn.send(request.SerializeToString())
                teste = self.conn.recv(2048)
                response = self.new_response(teste)
                print('\n===================================')
                if response.error_code:
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                elif len(response.academic_code):
                    for i in range(len(response.academic_code)):
                        print('{} - {}'.format(response.academic_code[i],
                                            response.academic_name[i]))
                else:
                    print('Sem resultados')
                print('===================================\n')
            elif 'define_nota' in args[0].lower():
                semester_year = args[3].split('/')
                request = self.new_request(
                    1, 'grade', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), float(args[4]))
                self.conn.send(request.SerializeToString())
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    print('Nota definida com sucesso')
                print('===================================\n')
            elif 'remove_nota' in args[0].lower():
                semester_year = args[3].split('/')
                request = self.new_request(
                    2, 'grade', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), None)
                self.conn.send(request.SerializeToString())
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    print('Nota removida com sucesso')
                print('===================================\n')
            elif 'define_falta' in args[0].lower():
                semester_year = args[3].split('/')
                request = self.new_request(
                    1, 'absences', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), float(args[4]))
                self.conn.send(request.SerializeToString())
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    print('Faltas definida com sucesso')
                print('===================================\n')
            elif 'remove_falta' in args[0].lower():
                semester_year = args[3].split('/')
                request = self.new_request(
                    2, 'absences', args[1], int(semester_year[0]),
                    int(semester_year[1]), int(args[2]), None)
                self.conn.send(request.SerializeToString())
                response = self.new_response(self.conn.recv(2048))
                print('\n===================================')
                if response.error_code:
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    print('Faltas removidas com sucesso')
                print('===================================\n')
            else:
                print('\nComando inválido\n')
