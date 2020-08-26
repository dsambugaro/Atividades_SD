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
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.connect((self.host, self.port))
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

    def start(self):
        """Interacts with server"""
        log.info('Client started')
        if not self.connected:
            log.error('Client not connected')
            exit(1)

        self.show_help()

        while True:
            command = input('Comando: ')
            if 'sair' == command.lower():
                break
            else:
                print('\nComando inválido\n')
