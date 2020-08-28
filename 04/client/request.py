class Request:
    """Class representing a request"""
    
    action = None  # 1 - set, 2 - remove or 3 - query
    target = None  # target of action
    academic_code = None  # student id
    course_code = None  # course id
    academic_year = None  # academic year
    academic_semester = None  # academic semester
    value = None  # value to set

    def __init__(self, action=None, target=None,
                 academic_code=None, course_code=None,
                 academic_year=None, academic_semester=None,
                 value=None):
        self.action = action
        self.target = target
        self.academic_code = academic_code
        self.course_code = course_code
        self.academic_year = academic_year
        self.academic_semester = academic_semester
        self.value = value

    def get_action(self):
        return self.action

    def set_action(self, value):
        self.action = value
    
    def get_target(self):
        return self.target

    def set_target(self, value):
        self.target = value
    
    def get_academic_code(self):
        return self.academic_code

    def set_academic_code(self, value):
        self.academic_code = value
    
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
    
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value