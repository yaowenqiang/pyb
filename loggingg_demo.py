import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('employee.log')
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
# logging.basicConfig(level=logging.DEBUG,filename='test.log',format='%(asctime)s:%(levelname)s:%(message)s')
def add(x, y):
	return x + y

def substract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	try:
		return x / y
	except ZeroDivisionError:
		logger.exception('trying to divide by zero')
	else:
		return result

num_1 = 10	
num_2 = 20
add_result = add(num_1, num_2)
# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
divide(1,0)