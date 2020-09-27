#!/usr/bin/env python3

import Pyro4

from grade import Grade
from absences import Absences
from course import Course

daemon = Pyro4.Daemon()                  
ns = Pyro4.locateNS()                    
uri_grade = daemon.register(Grade)
uri_grade = daemon.register(Absences)
uri_grade = daemon.register(Course)

ns.register("GradeService", uri_grade)
ns.register("AbsencesService", uri_grade)
ns.register("CourseService", uri_grade)

print("Server started")
daemon.requestLoop()                     
