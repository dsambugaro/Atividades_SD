from database import DB

db = DB()

def response(status=200, data=[], msg='', error_code=0):
    
    return {
        "status": status,
        "data": data,
        "error_code": error_code,
        "error_message": msg
    }

def validate_course(course):
    if not course:
        return False

    if not len(db.get_course(course)):
        return False
    
    return True

def validate_enrolle(course, semester, year, student):
    if not course:
        return False

    if not len(db.get_enrolle(course, semester, year, student)):
        return False
    
    return True

def validate_course_and_enrolle(course, semester, year, student):
    return validate_course(course) and validate_enrolle(course, semester, year, student)