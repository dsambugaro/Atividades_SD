# Course class

import utils
from database import DB


class Course:
    def __init__(self):
        self.db = DB()

    def gradesAndAbsences(self, course, semester, year):
        if utils.validate_course(course):
            data = self.db.get_grades_absences(course, semester, year)
            return utils.response(200, data)
        else:
            return utils.response(404, [], 404, "Disciplina '{}' não encontrada".format(course))

    def students(self, course, semester, year):
        if utils.validate_course(course):
            data = self.db.list_students(course, semester, year)
            return utils.response(200, data)
        else:
            return utils.response(404, [], 404, "Disciplina '{}' não encontrada".format(course))
            
