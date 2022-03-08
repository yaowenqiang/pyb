def prefix_decorator(prefix):
	def decorator_function(original_function):
		def wrapper_function(*args, **kwargs):
			print(prefix, 'Executed before', original_function.__name__)
			result = original_function(*args, **kwargs)
			print(prefix, 'Executed After', original_function.__name__, '\n')
			return result
		return wrapper_function
	return decorator_function

# @decorator_function
@prefix_decorator('TEXTING:')
def display_info(name, age):
	print('display_info run with arguments ({}, {})'.format(name, age))

display_info('John', 20)
display_info('Jack', 30)