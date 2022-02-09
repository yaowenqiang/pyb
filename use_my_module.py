import sys
import random
import math
import datetime
import calendar
import os
import antigravity
# import modules as mm;
# from modules import *
# sys.path.append('/Users/')
from modules import find_index as fi, test

courses = ['history', 'Math', 'Phsics', 'compsci']

# index = mm.find_index(courses, 'Math')
index = fi(courses, 'Math')
print(index)

print(test)

print(sys.path)

# ~/.bash_profile
# export PYTHONPATH="/newLocation"

print(random.choice(courses))
print(math.radians(90))

print(datetime.date.today())

print(calendar.isleap(2020))

print(os.getcwd())

print(os.__file__)
