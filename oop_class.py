
class Employee():
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@compay.com'
		Employee.num_of_emps += 1


	def fullname(self):
		return '{} {}'.format(self.first, self.last)

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




emp_1 = Employee('jack', 'yao', 2000)
emp_2 = Employee('text', 'user',4000)

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
print(emp_1.fullname())

print(Employee.fullname(emp_2))


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