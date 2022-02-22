# python -m unittest test_calc.py

import unittest

import calc

class testCalc(unittest.TestCase):

	def test_add(self):
		# result = calc.add(10, 5)
		self.assertEqual(calc.add(10,5), 15)
		self.assertEqual(calc.add(-1,1), 0)
		self.assertEqual(calc.add(-1,-1), -2)

	def test_divide(self):
		# self.assertRaises(ValueError,calc.divide,0,0)

		with self.assertRaises(ValueError):
			calc.divide(0,0)


if __name__ == '__main__':
	unittest.main()