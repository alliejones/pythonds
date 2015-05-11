def gcd(m, n):
	while m % n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n
	return n

class Fraction:

	def __init__(self, top, bottom):
		self.num = top;
		self.den = bottom;

	def __str__(self):
		return str(self.num)+"/"+str(self.den);

	def _make_simplified_fraction(self, num, den):
		cd = gcd(num, den)
		return Fraction(num//cd, den//cd)

	def __add__(self, other):
		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den
		return self._make_simplified_fraction(new_num, new_den)

	def __sub__(self, other):
		new_num = self.num * other.den - self.den * other.num
		new_den = self.den * other.den
		return self._make_simplified_fraction(new_num, new_den)

	def __mul__(self, other):
		new_num = self.num * other.num
		new_den = self.den * other.den
		return self._make_simplified_fraction(new_num, new_den)

	def __div__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num
		return self._make_simplified_fraction(new_num, new_den)

	def _common_terms(self, other):
		return (self.num * other.den, other.num * self.den)

	def __eq__(self, other):
		first, second = self._common_terms(other)
		return first == second

	def __lt__(self, other):
		first, second = self._common_terms(other)
		return first < second

	def __gt__(self, other):
		first, second = self._common_terms(other)
		return first > second
