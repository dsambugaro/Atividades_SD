# Absences class

import Pyro4

import utils
from database import DB

@Pyro4.expose
class Absences:
    def __init__(self):
        self.db = DB()
    
    def create(self, course, semester, year, student, absences):
        self.update(course, semester, year, student, absences)
    
    def read(self, course, semester, year, student):
        if utils.validate_course(course):
            if utils.validate_enrolle(course, semester, year, student):
                data = self.db.get_student_absences(course, semester, year, student)
                return utils.response(200, data)
            else:
                return utils.response(404, [], 404, "Matricula do aluno '{}' no curso '{}' não encontrada".format(student, course))
        else:
            return utils.response(404, [], 404, "Disciplina '{}' não encontrada".format(course))
    
    def update(self, course, semester, year, student, absences):
        if utils.validate_course(course):
            if utils.validate_enrolle(course, semester, year, student):
                data = self.db.set_student_absences(course, semester, year, student, absences)
                return utils.response(200, data)
            else:
                return utils.response(404, [], 404, "Matricula do aluno '{}' no curso '{}' não encontrada".format(student, course))
        else:
            return utils.response(404, [], 404, "Disciplina '{}' não encontrada".format(course))
    
    def delete(self, course, semester, year, student):
        if utils.validate_course(course):
            if utils.validate_enrolle(course, semester, year, student):
                data = self.db.remove_student_absences(course, semester, year, student)
                return utils.response(200, data)
            else:
                return utils.response(404, [], 404, "Matricula do aluno '{}' no curso '{}' não encontrada".format(student, course))
        else:
            return utils.response(404, [], 404, "Disciplina '{}' não encontrada".format(course))
