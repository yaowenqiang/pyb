class Employee():
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@compay.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)




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