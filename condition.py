if True:
	print('conditional was true')

if False:
	print('conditional was true')



language = 'python'

if language == 'python':
	print('language is python')
elif language == 'java':
	print('language is java')
else:
	print('no match')



user = 'Admin'
logged_in = True

if user == 'Admin' and  logged_in:
	print('Admin Page')
else:
	print('bad credit')


if not logged_in:
	print('pleas log in')
else:
	print('welcome')


a = {1,2,3}
b = {1,2,3}

print(a == b)


print(a is b)


print(id(a))
print(id(b))



# False condition

# False
# None
# Zero of any numeric type
# Any empty sequence, For example '', [], (),
# Any empty mapping For example, {},


confition = set()

if confition:
	print('Evaluated to True')
else:
	print('Evaluated to False')