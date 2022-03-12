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