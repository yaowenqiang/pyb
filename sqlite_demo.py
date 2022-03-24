import sqlite3
from employee import Employee


# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')
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
conn.close()
