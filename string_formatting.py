import datetime
person = {
	'name':'jack',
	'age': 20
}

sentance  = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentance)

tag = 'h1'
text = 'This is a headline'

sentance2 = '<{0}>{1}<{0}>'.format(tag, text)
print(sentance2)


# sentance3  = 'My name is {0[name]} and I am {1[age]} years old'.format(person, person)
sentance3  = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentance)

sentance4  = 'My name is {name} and I am {age} years old'.format(name='jack', age=20)
print(sentance4)


sentance5  = 'My name is {name} and I am {age} years old'.format(**person)
print(sentance5)


for i in range(1, 11):
	sentance6 = 'The value is {:03}'.format(i)
	print(sentance6)


pi = 3.14159265
sentance7 = 'Pi is equal to {:.2f}'.format(pi)
print(sentance7)

# sentance8 = '1 MB is equal to {:,} bytes'.format(1000**2)
sentance8 = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentance8)


my_date = datetime.datetime(2022, 3, 1, 12, 30, 45)
sentance9 = '{:%B %d %Y}'.format(my_date)
print(sentance9)

sentance10 = '{0:%B %d %Y} on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentance10)