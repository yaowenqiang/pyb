try:
	f = open('test.txt')
	if f.name == '':
		raise Exception
	# var = bad_var
except FileNotFoundError as e:
	# print('_Error! file does not exist')
	print(e)
except Exception as e:
	# print('Sorry, someting went wrong!')
	print(e)
else:
	print(f.read())
	f.closed()
finally:
	print('Executing Finally...')
