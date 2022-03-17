
class Employee():
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		# self.email = first + '.' + last + '@compay.com'
		Employee.num_of_emps += 1


	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split('.')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('delete name')
		self.first = None
		self.last = None

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	def apply_raise(self):
		# self.pay = int(self.pay * Employee.raise_amount)
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first ,last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5  or  day.weekday() == 6:
			return False
		return True

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
			

	def __str__(self):
		return '{} - {}'.format(self.fullname, self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self,):
		return len(self.fullname)



emp_1 = Employee('jack', 'yao', 2000)
print(emp_1)

print(str(emp_1))
print(repr(emp_1))
print(int.__add__(100, 200))
print(str.__add__('a', 'b'))
emp_2 = Employee('text', 'user',4000)

print(emp_2 + emp_1)
print(len(emp_1))

# emp_1.first = 'jack'
# emp_1.last = 'yao'
# emp_1.email = 'jack@yao.com'
# emp_1.pay = 5000


# emp_2.first = 'text'
# emp_2.last = 'User'
# emp_2.email = 'text@yao.com'
# emp_2.pay = 8000

print(emp_1)
print(emp_2)
print(emp_1.fullname)

# print(Employee.fullname(emp_2))


emp_2.apply_raise()
print(emp_2.pay)

print(emp_2.raise_amount)
print(emp_1.raise_amount)
print(Employee.raise_amount)

print(emp_2.__dict__)
print(emp_1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05
print(emp_2.raise_amount)
print(emp_1.raise_amount)
print(Employee.raise_amount)

emp_1.raise_amount = 1.06
print(emp_1.raise_amount)
print(Employee.raise_amount)

print(Employee.num_of_emps)




Employee.set_raise_amt(2.0)
# emp_1.set_raise_amt(3.0)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-doe-5000'
emp_str_2 = 'Steve-Smith-12000'
emp_str_3 = 'Jane-Doe-52000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)

import datetime

my_date = datetime.date(2022, 3, 15)
print(Employee.is_workday(my_date))



class Developer(Employee):
	raise_amount = 1.10
	def __init__(self, first, last, pay, program_language):
		super().__init__(first, last, pay)
		# Employee.__init__(self, first, last, pay)
		self.program_language = program_language

class Manager(Employee):
	def __init__(self, first, last, pay, employees = None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_employees(self):
		for emp in self.employees:
			print('-->', emp.fullname)


dev_1 = Developer('leo', 'li', 20000, 'python')
dev_2 = Developer('bruce', 'pan', 12000, 'java')
print(dev_1.email)
print(dev_2.email)

print(dev_1.program_language)
print(dev_2.program_language)

# print(help(Developer))

mgr_1 = Manager('Sue', 'Smith', 30000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_employees()
mgr_1.remove_emp(dev_2)
mgr_1.print_employees()


print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Employee))