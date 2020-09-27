#!/usr/bin/env python3

import Pyro4

from grade import Grade
from absences import Absences
from course import Course

daemon = Pyro4.Daemon()                  
uri_grade = daemon.register(Grade)
uri_absences = daemon.register(Absences)
uri_course = daemon.register(Course)

print('URI Grade: {}'.format(uri_grade))
print('URI Absences: {}'.format(uri_absences))
print('URI Course: {}'.format(uri_course))

print("Server started")
daemon.requestLoop()                     
