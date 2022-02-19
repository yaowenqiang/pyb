from operator import attrgetter


li = [1,4,5,7,4,3,2,5,6,7,8]

s_li = sorted(li, reverse=True)
li.sort()
print("Sorted Variables: \t", s_li)
print("Original Variables: \t", li)




tu = (1,4,5,7,4,3,2,5,6,7,8)

su_tu = sorted(tu)
print(su_tu)


di = {'name':'Corey', 'job':'Programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print(s_di)

li_2 = [-5, -10, -1000, 1,2,6,4,3,32]
s_li_2 = sorted(li_2)
print(s_li_2)

s_li_2 = sorted(li_2, key=abs)
print(s_li_2)


class employee():
	"""docstring for employee"""
	def __init__(self, name, age, salary):
		super(employee, self).__init__()
		self.name = name
		self.age = age
		self.salary = salary
		

	def __repr__(self):
		return '({}, {}, ${})'.format(self.name, self.age, self.salary)

e1 = employee('carl', 27, 18000)
e2 = employee('John', 32, 180000)
e3 = employee('Jack', 27, 1800000)


employees = [e1, e2, e3]


def e_sort(employee):
	return employee.name


# s_employees = sorted(employees, key=e_sort, reverse=True)

# s_employees = sorted(employees, key=lambda e: e.name)

s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)





