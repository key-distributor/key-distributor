# 133 bit prime -- for use with 12 word mnemonics
P12 = 5444517870735015415413993718908291383363

# 166 bit prime -- for use with 15 word mnemonics
P15 = 46768052394588893382517914646921056628989841375373

# 199 bit prime -- for use with 18 word mnemonics
P18 = 401734511064747568885490523085290650630550748445698208825359

# 232 bit prime -- for use with 21 word mnemonics
P21 = 3450873173395281893717377931138512726225554486085193277581262111899753

# 265 bit prime -- for use with 24 word mnemonics
P24 = 29642774844752946028434172162224104410437116074403984394101141506025761187823791

def field_generator(length):
	"""returns proper instance of FiniteField class.
	assumes length is 12, 15, 18, 21, or 24"""

	class FiniteField:
		"""Finite Field class"""
		if length == 12: prime = P12
		elif length == 15: prime = P15
		elif length == 18: prime = P18
		elif length == 21: prime = P21
		else: prime = P24

		def __init__(self, val):
			self.val = val % FiniteField.prime

		def __eq__(self, other):
			return self.val == other.val

		def __add__(self, other):
			return FiniteField(self.val + other.val)

		def __neg__(self):
			return FiniteField(-self.val)

		def __sub__(self, other):
			return self + (-other)

		def __mul__(self, other):
			return FiniteField(self.val * other.val)

		def __truediv__(self, other):
			return self * other.inverse()

		def __pow__(self, exp):
			return FiniteField(pow(self.val, exp, FiniteField.prime))

		def __repr__(self):
			return str(self.val)

		def __int__(self):
			return self.val

		def inverse(self):
			"""computes inverse. fermats little thm is better suited against timing attacks than xgcd"""
			return self ** (FiniteField.prime-2)

	return FiniteField




