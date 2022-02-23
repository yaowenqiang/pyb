import unittest
from unittest.mock import patch

from employee import Employee

class TestEmployee(unittest.TestCase):

	"""docstring for TestEmployee"""

	def setUpClass():
		print("setUpClass")

	def tearDownClass():
		print('tearDownClass')

	def setUp(self):
		self.emp_1 = Employee('Goney', 'Schafer', 50000)
		self.emp_2 = Employee('Jack', 'Smith', 78000)

	def tearDown(self):
		pass

	def test_email(self):

		self.assertEqual(self.emp_2.email, 'Jack.Smith@email.com')
		self.assertEqual(self.emp_1.email, 'Goney.Schafer@email.com')

	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')


			mocked_get.assert_called_with('http://company.com/Schafer/May')

			self.assertEqual(schedule, 'Success')


		
		


if __name__ == '__main__':
	unittest.main()
