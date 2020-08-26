class Message:
    """Class representing a message"""
    
    msg_type = None  # 1 - request or 2 - response
    action = None  # 1 - set, 2 - remove or 3 - query
    academics_codes = None  # students ids
    course_code = None  # course id
    academic_year = None  # academic year
    academic_semester = None  # academic semester
    grade = None  # grade to set
    absences = None  # absences to set

    def __init__(self, msg_type=1, action=3,
                 academics_codes=[], course_code=None,
                 academic_year=None, academic_semester=None,
                 grade=None, absences=None):
        self.msg_type = msg_type
        self.action = action
        self.academics_codes = academics_codes
        self.course_code = course_code
        self.academic_year = academic_year
        self.academic_semester = academic_semester
        self.grade = grade
        self.absences = absences

    def get_msg_type(self):
        return self.msg_type

    def set_msg_type(self, value):
        self.msg_type = value

    def get_action(self):
        return self.action

    def set_action(self, value):
        self.action = value
    
    def get_academics_codes(self):
        return self.academics_codes

    def set_academics_codes(self, value):
        self.academics_codes = value
    
    def get_course_code(self):
        return self.course_code

    def set_course_code(self, value):
        self.course_code = value
    
    def get_academic_year(self):
        return self.academic_year

    def set_academic_year(self, value):
        self.academic_year = value
    
    def get_academic_semester(self):
        return self.academic_semester

    def set_academic_semester(self, value):
        self.academic_semester = value
    
    def get_grade(self):
        return self.grade

    def set_grade(self, value):
        self.grade = value
    
    def get_absences(self):
        return self.absences

    def set_absences(self, value):
        self.absences = value