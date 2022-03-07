def outer_function(msg):
	# message = msg

	def inner_function():
		print(msg)

	# return inner_function()
	return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('bye')
hi_func()
bye_func()


def decorator_function(original_function):
	def wrapper_function():
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function()
	return wrapper_function


@decorator_function
def display():
	print('display function ran')

decorated_display = decorator_function(display)

decorated_display()
