from random import SystemRandom
from FiniteField import field_generator
from Secret import Secret

class Polynomial:

	def __init__(self, k, n, m):
		"""For (k, n) scheme to share secret s"""
		self.degree = k-1
		self.points = n
		self.Fp = field_generator(len(m))
		self.coeffs = [self.Fp(int(m))] + [self.Fp(SystemRandom().randrange(0, self.Fp.prime)) for _ in range(k-1)]

	def __call__(self, x):
		"""returns polynomial instance evaluated at x"""
		res = self.Fp(0)
		for i in range(self.degree + 1):
			res = self.coeffs[-(i+1)] + self.Fp(x)*res
		return res

	def secrets(self):
		"""generator that returns polynomial evaluated at points 1, ..., n"""
		for i in range(1, self.points+1):
			yield i, int(self(i))

def interpolate(pairs, message_length):
	"""Recovers secret as an integer. message_length is length of mnemonic
	being recoverd. Uses lagrange polynomial"""
	Fp = field_generator(message_length)
	X, Y = zip(*pairs) # vectors of x's and y's
	secret = Fp(0)
	for i in range(len(X)):
		num, den = Fp(1), Fp(1)
		for j in range(len(X)):
			if i != j:
				num *= Fp(X[j])
				den *= Fp(X[j] - X[i])
		secret += num / den * Fp(Y[i])

	return int(secret)
