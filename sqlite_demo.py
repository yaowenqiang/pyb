import sqlite3

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
conn.close()