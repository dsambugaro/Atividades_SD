# RMI client

import os
import logging as log

import Pyro4


class Client:
    """RMI Client"""
    host = None
    port = None
    connected = False

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._setup_log()
        self._connect()

    def _setup_log(self):
        """Configures log format and level"""
        log.basicConfig(format='[ %(levelname)s ] %(message)s', level=log.INFO)

    def _connect(self):
        """Connects to a RMI server"""
        Pyro4.locateNS(self.host, self.port)
        self.gradeService = Pyro4.Proxy("PYRONAME:GradeService")
        self.absencesService = Pyro4.Proxy("PYRONAME:AbsencesService")
        self.courseService = Pyro4.Proxy("PYRONAME:CourseService")
        self.connected = True
        log.info('Client connected to %s:%s', self.host, self.port)

    def show_help(self):
        """Prints commands list on console"""
        print('* * * * * * * * * * * * * MENU * * * * * * * * * * * * *')
        print('MOSTRAR_NOTA <cod. disciplina> <RA> <ano/semestre> <nota>\n\tMostra a nota do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('ATUALIZAR_NOTA <cod. disciplina> <RA> <ano/semestre> <nota>\n\tAtualiza a nota do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('INSERIR_NOTA <cod. disciplina> <RA> <ano/semestre> <nota>\n\tDefine a nota do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('REMOVER_NOTA <cod. disciplina> <RA> <ano/semestre>\n\tRemove a nota do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('MOSTRAR_FALTAS <cod. disciplina> <RA> <ano/semestre> <faltas>\n\tMostra as faltas do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('ATUALIZAR_FALTAS <cod. disciplina> <RA> <ano/semestre> <faltas>\n\tAtualiza as faltas do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('INSERIR_FALTAS <cod. disciplina> <RA> <ano/semestre> <faltas>\n\tDefine as faltas do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('REMOVER_FALTAS <cod. disciplina> <RA> <ano/semestre>\n\tRemove as faltas do aluno RA numa dada disciplina num dado semestre e ano letivo\n')
        print('LISTAR_NOTAS_FALTAS <cod. disciplina> <ano/semestre>\n\tLista as notas e faltas dos alunos numa dada disciplina num dado semestre e ano letivo\n')
        print('LISTAR_ALUNOS <cod. disciplina> <ano/semestre>\n\tLista os alunos numa dada disciplina num dado semestre e ano letivo\n')
        print('AJUDA\n\tMostra esse texto\n')
        print('SAIR\n\tFecha o cliente\n')
        print('* * * * * * * * * * * * * *  * * * * * * * * * * * * * *')

    def new_request(self, course_code, academic_semester,
                    academic_year, academic_code, grade, absences):
        """Creates a new request from args"""
        course_code = course_code if course_code else ''  # default: ''
        academic_semester = academic_semester if academic_year else 0  # default: 0
        academic_year = academic_year if academic_year else 0  # default: 0
        academic_code = academic_code if academic_code else 0  # default: 0
        grade = grade if grade else 0.0  # default: 0.0
        absences = absences if absences else 0  # default: 0
        return None

    def start(self):
        """Interacts with server"""
        log.info('Client started')
        if not self.connected:
            log.error('Client not connected')
            exit(1)

        # Prints menu
        self.show_help()

        grade = self.gradeService
        absences = self.absencesService
        course = self.courseService

        while True:
            command = input('Comando: ')
            args = command.split(' ')  # Split args from input
            if 'sair' == args[0].lower():
                break  # Exit client
            elif 'ajuda' in args[0].lower():
                self.show_help()
            elif 'listar_alunos' in args[0].lower():
                semester_year = args[2].split('/')  # Get semester and year
                response = course.students(args[1], int(semester_year[0]),
                                           int(semester_year[1]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                elif len(response.data):
                    # Print results
                    print('RA - NOME')
                    for i in range(len(response.data)):
                        print('{} - {}'.format(response.academic_code[i],
                                               response.academic_name[i]))
                else:
                    # Print this msg if no results are found
                    print('Sem resultados')
                print(
                    '======================================================================\n')
            elif 'listar_notas_faltas' in args[0].lower():
                semester_year = args[2].split('/')  # Get semester and year
                response = course.gradesAndAbsences(args[1], int(semester_year[0]),
                                                    int(semester_year[1]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                elif len(response.data):
                    # Print results
                    print('RA\tNOTA\tFALTAS')
                    for i in range(len(response.data)):
                        print('{}\t{:.2f}\t{}'.format(response.academic_code[i],
                                                      response.grade[i], response.absences[i]))
                else:
                    # Print this msg if no results are found
                    print('Sem resultados')
                print(
                    '======================================================================\n')
            elif 'mostrar_nota' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = grade.read(args[1], int(semester_year[0]),
                                      int(semester_year[1]), int(args[2]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                elif response.grade:
                    # Print succes
                    print('{:.2f}'.format(response.grade[0]))
                else:
                    # Print this msg if no results are found
                    print('Sem resultados')
                print(
                    '======================================================================\n')
            elif 'atualizar_nota' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = grade.update(args[1], int(semester_year[0]),
                                        int(semester_year[1]), int(
                    args[2]), float(args[4]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Nota atualizada com sucesso')
                print(
                    '======================================================================\n')
            elif 'inserir_nota' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = grade.create(args[1], int(semester_year[0]),
                                        int(semester_year[1]), int(
                    args[2]), float(args[4]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Nota inserida com sucesso')
                print(
                    '======================================================================\n')
            elif 'remover_nota' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = grade.delete(args[1], int(semester_year[0]),
                                        int(semester_year[1]), int(args[2]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Nota removida com sucesso')
                print(
                    '======================================================================\n')
            elif 'mostrar_faltas' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = absences.read(args[1], int(semester_year[0]),
                                         int(semester_year[1]), int(args[2]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                elif response.absences:
                    # Print succes
                    print('{}'.format(response.absences[0]))
                else:
                    # Print this msg if no results are found
                    print('Sem resultados')
                print(
                    '======================================================================\n')
            elif 'atualizar_faltas' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = absences.update(args[1], int(semester_year[0]),
                                           int(semester_year[1]), int(args[2]), int(args[4]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Número de Faltas atualizado com sucesso')
                print(
                    '======================================================================\n')
            elif 'inserir_falta' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = absences.create(args[1], int(semester_year[0]),
                                           int(semester_year[1]), int(args[2]), int(args[4]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Número de faltas inserido com sucesso')
                print(
                    '======================================================================\n')
            elif 'remover_faltas' in args[0].lower():
                semester_year = args[3].split('/')  # Get semester and year
                response = absences.delete(args[1], int(semester_year[0]),
                                           int(semester_year[1]), int(args[2]))
                print(
                    '\n======================================================================')
                if response.error_code:
                    # Print error
                    print('Erro {} - {}'.format(response.error_code,
                                                response.error_message))
                else:
                    # Print succes
                    print('Número de faltas removido com sucesso')
                print(
                    '======================================================================\n')
            else:
                # Command invalid
                print('\nComando inválido\n')
