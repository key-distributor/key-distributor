from word_maps import ENG

class Phrase:
	"""Represents a mnemonic, whether that be a backup mnemonic or a share of the secret"""

	def __init__(self, phrase):
		self.phrase = phrase.lower().split()

	def __len__(self):
		return len(self.phrase)

	def __repr__(self):
		return " ".join(self.phrase)

	def __int__(self):
		"""Maps a phrase to an integer in [0, pow(2, len*11) - 1]

		HEADS UP: phrases like 'anchor often crush bundle twice sniff dilemma prize wing ten deposit abandon',
		'anchor often crush bundle twice sniff dilemma prize wing ten abandon abandon', and
		'anchor often crush bundle twice sniff dilemma prize wing abandon abandon abandon' will
		map to the same int. This doesn't cause any problems."""
		num = 0
		for i, word in enumerate(self.phrase):
			num += ENG.get_index(word) << (i*11)

		return num