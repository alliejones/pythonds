import unittest

from fraction import Fraction

class FractionTest(unittest.TestCase):
	def test_add(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(3, 4)
		f3 = f1 + f2

		self.assertEqual(f3.get_num(), 5)
		self.assertEqual(f3.get_den(), 4)

	def test_sub(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 4)
		f3 = f1 - f2

		self.assertEqual(f3.get_num(), 1)
		self.assertEqual(f3.get_den(), 4)

	def test_mult(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 4)
		f3 = f1 * f2

		self.assertEqual(f3.get_num(), 1)
		self.assertEqual(f3.get_den(), 8)

	def test_div(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 4)
		f3 = f1 / f2

		self.assertEqual(f3.get_num(), 2)
		self.assertEqual(f3.get_den(), 1)

	def test_eq(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 2)
		f3 = Fraction(1, 3)

		self.assertTrue(f1 == f2)
		self.assertFalse(f1 == f3)

	def test_ne(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 2)
		f3 = Fraction(1, 3)

		self.assertTrue(f1 != f3)
		self.assertFalse(f1 != f2)

	def test_lt(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 3)

		self.assertTrue(f2 < f1)
		self.assertFalse(f1 < f2)

	def test_le(self):
		f1 = Fraction(1, 2)
		f2 = Fraction(1, 2)
		f3 = Fraction(1, 3)

		self.assertTrue(f1 <= f2)
		self.assertTrue(f3 <= f1)
		self.assertFalse(f1 <= f3)

	def test_gt(self):
		f1 = Fraction(1, 3)
		f2 = Fraction(1, 2)

		self.assertTrue(f2 > f1)
		self.assertFalse(f1 > f2)

	def test_ge(self):
		f1 = Fraction(1, 3)
		f2 = Fraction(1, 3)
		f3 = Fraction(1, 2)

		self.assertTrue(f2 >= f1)
		self.assertTrue(f3 >= f1)
		self.assertFalse(f1 >= f3)


if __name__ == '__main__':
    unittest.main()