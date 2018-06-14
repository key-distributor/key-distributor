LOW_INDEX = 0
HIGH_INDEX = 2047

class Map(list):
	"""Map between word list and integers. offers quick look up of either word or int.
	Assumes internal list is sorted and of length HIGH_INDEX - LOW_INDEX + 1.

	a = Map(word_list)
	a.get_word(index) # returns word associated with index
	a.get_index(word) # returns index associated with word
	"""


	def get_word(self, index):
		"""Returns word a index. Assumes index is between global variables LOW_INDEX and HIGH_INDEX."""
		return self[index]

	def get_index(self, word):
		"""returns index associated with word if it exists, -1 otherwise."""

		low = LOW_INDEX
		high = HIGH_INDEX
		
		while low <= high:
			mid = (high + low) // 2
			if self[mid] == word:
				return mid
			else:
				if word < self[mid]:
					high = mid - 1
				else:
					low = mid + 1
		return -1
