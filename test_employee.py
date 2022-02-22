import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

	"""docstring for TestEmployee"""


	def setUp(self):
		self.emp_1 = Employee('Goney', 'Schafer', 50000)
		self.emp_2 = Employee('Jack', 'Smith', 78000)

	def tearDown(self):
		pass

	def test_email(self):

		self.assertEqual(self.emp_2.email, 'Jack.Smith@email.com')
		self.assertEqual(self.emp_1.email, 'Goney.Schafer@email.com')
		
		


if __name__ == '__main__':
	unittest.main()
