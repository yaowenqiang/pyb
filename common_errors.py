from math import radians, sin
from datetime import datetime
import time

nums = [11, 33, 55, 33]
for num in nums:
	square = num ** 2
	print(square)




rads = radians(90)

print(sin(rads))


# def add_employee(emp, emp_list=[]):
# 	emp_list.append(emp)
# 	print(emp_list)


def add_employee(emp, emp_list=None):
	if emp_list is None:
		emp_list = []

	emp_list.append(emp)
	print(emp_list)

emps = ['John', 'Jack']

add_employee('joy', emps)

add_employee('Corey')
add_employee('Smith')
add_employee('Scott')


# def display_time(time = datetime.now()):
# 	print(time.strftime('%B %d, %Y %H:%M:%S'))

def display_time(time = None):
	if time == None:
		time =  datetime.now()

	print(time.strftime('%B %d, %Y %H:%M:%S'))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()


names = ['Peter Parker', 'clark Kent', 'Wade Whilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = zip(names, heroes)
identities2 = identities
print(identities)

print(list(identities))


for identity in identities2:
	print('{} is actually {}'.format(identity[0], identity[1]))