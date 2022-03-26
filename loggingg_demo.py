import logging

logging.basicConfig(level=logging.DEBUG,filename='test.log',format='%(asctime)s:%(levelname)s:%(message)s')
def add(x, y):
	return x + y

def substract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

num_1 = 10	
num_2 = 20
add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))