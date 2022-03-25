import sqlite3
from employee import Employee


# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')
# debug
conn.set_trace_callback(print)
c = conn.cursor()
# c.execute('''CREATE TABLE employee(
# 			first text,
# 			last text,
# 			pay integer	
# 			)''')

# c.execute("insert into employee values('jack', 'yao', 5000)")

c.execute('select * from employee where last = "yao"')
print(c.fetchone())
# c.fetchmany()
# c.fetchall()
conn.commit()


emp_1 = Employee('john', 'Doe', 8000)
emp_2 = Employee('jacky', 'yao', 8000)

c.execute('INSERT INTO employee VALUES(:first, :last, :pay)',{'first': emp_1.first, 'last': emp_1.last, 'pay':emp_1.pay})
conn.commit()
# conn.close()


def insert_emp(emp):
	with conn:
		c.execute('INSERT INTO employee VALUES(:first, :last, :pay)',{'first': emp.first, 'last': emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
	c.execute('select * from employee where last = :last', {'last': lastname})
	return c.fetchall()

def update_apy(name, pay):
	with conn:
		c.execute('''update employee set pay = :pay 
			where first = :first and last = :last''',
			{'first':emp.first,'last': emp.last, 'pay': emp.pay}
		)

def remove_emp(emp):
	with conn:
		c.execute('''delete from employee where first = :first and last = :last''',
			{'first':emp.first,'last': emp.last,}
		)



insert_emp(emp_1)
emp = get_emps_by_name('yao')
print(emp)