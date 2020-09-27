# DB class

import sqlite3


class DB:
    def __init__(self):
        self.conn = None
        self.db_name = 'gerenciamento_notas.db'

    def _connect(self):
        self.conn = sqlite3.connect(self.db_name)

    def _close(self):
        self.conn.close()
    
    def _execute_query(self, sqlquery, params):
        self._connect()
        result = self.conn.execute(sqlquery, params)
        self._close()
        return result

    def get_course(self, code):
        sqlquery = "SELECT * FROM disciplina WHERE codigo = ?"
        params = [code]
        return self._execute_query(sqlquery, params)
    
    def get_enrolle(self, course, semester, year, student):
        sqlquery = "SELECT * FROM matricula WHERE ano = ? AND semestre = ? and cod_disciplina = ? and ra_aluno = ?"
        params = [year, semester, course, student]
        return self._execute_query(sqlquery, params)
    
    def list_students(self, course, semester, year):
        sqlquery = "SELECT ra, nome from aluno WHERE ra IN (SELECT ra_aluno FROM matricula WHERE cod_disciplina = ? AND semestre = ? AND ano = ?)"
        params = [course, semester, year]
        return self._execute_query(sqlquery, params)
    
    def get_grades_absences(self, course, semester, year):
        sqlquery = "SELECT ra_aluno, nota, faltas FROM matricula WHERE ano = ? AND semestre = ? AND cod_disciplina = ?"
        params = [year, semester, course]
        return self._execute_query(sqlquery, params)

    def get_student_grade(self, course, semester, year, student):
        sqlquery = "SELECT nota FROM matricula WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
        params = [year, semester, course, student]
        return self._execute_query(sqlquery, params)

    def set_student_grade(self, course, semester, year, student, grade):
        sqlquery = "UPDATE matricula SET nota = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
        params = [grade, year, semester, course, student]
        return self._execute_query(sqlquery, params)
    
    def remove_student_grade(self, course, semester, year, student):
        grade = 0
        sqlquery = "UPDATE matricula SET nota = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
        params = [grade, year, semester, course, student]
        return self._execute_query(sqlquery, params)

    def get_student_absences(self, course, semester, year, student):
        sqlquery = "SELECT faltas FROM matricula WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
        params = [year, semester, course, student]
        return self._execute_query(sqlquery, params)
    
    def set_student_absences(self, course, semester, year, student, absences):
        sqlquery = "UPDATE matricula SET faltas = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
        params = [absences, year, semester, course, student]
        return self._execute_query(sqlquery, params)
    
    def remove_student_absences(self, course, semester, year, student):
        absences = 0
        sqlquery = "UPDATE matricula SET faltas = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
        params = [absences, year, semester, course, student]
        return self._execute_query(sqlquery, params)
    


