from word_maps import ENG

class Secret:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return """
Secret # {0}
Passphrase: {1}
""".format(self.x, self.to_phrase())

	def to_phrase(self):
		return " ".join(ENG.get_word(n) for n in self._11_bits())

	def _11_bits(self):
		num = int(self.y)
		mask = (1 << 11) - 1
		while num:
			yield num & mask
			num = num >> 11