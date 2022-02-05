student = {
	'name':'john',
	'age': 25,
	'courses':['math', 'compsci'],
	1: 'number',
}

print(student)

print(student['name'])
print(student['courses'])
print(student[1])

print(student.get('phone','not found'))

student['phone'] = '555'
print(student.get('phone','not found'))

student.update(
	{
		'name':'new name',
		'age': 20
	}
)

print(student)


del student['age']
print(student)


name = student.pop('name')
print(name)

print(len(student))
print(student.keys())

print(student.values())
print(student.items())



for key, value in student.items():
	print(key, value)

