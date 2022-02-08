def hello_function(greeting, name='jack'):
	# print('hello function')
	# pass
	# return "{}, {}".format(greeting, name)
	return f"{greeting}, {name}"

# hello_function(greeting='hello function')


print(hello_function(greeting='hello').upper())

def student_info(*args, **kwargs):
	print(args)	
	print(kwargs)


student_info(1,2,3, age=4)


courses = ['Math', 'Art']

info = {'name':'John','age':20}

student_info(*courses, **info)



month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""Return true for Leap year, false for notn-leap year."""

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
	if not 1 <= month <= 12:
		return "Invalid Month"

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]


print(is_leap(2017))

print(is_leap(2020))

print(days_in_month(2017, 2))


