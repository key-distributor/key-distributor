import sys
from word_maps import ENG
from Polynomial import Polynomial, interpolate
from Phrase import Phrase


class Menu:

	def __init__(self):
		print("Welcome to KEY DISTRIBUTOR!")
		self.actions = {
			'1': self.distribute,
			'2': self.recover,
			'3': self.quit
			}

	def display_menu(self):
		print("Choose an action\n")
		print("1. Distribute")
		print("2. Recover")
		print("3. Quit")

	def run(self):
		"""run the menu"""
		while True:
			self.display_menu()
			choice = input("Choose an action: ")
			action = self.actions.get(choice)
			if action:
				action()
			else:
				print("{0} is not a valid choice.".format(choice))

	def distribute(self):
		k = get_threshold()
		n = get_no_secrets()
		mnem = get_phrase()
		share_secret(k, n, mnem)
		input("press enter to continue")

	def recover(self):
		L = get_mnem_length()
		k = get_threshold()
		secrets = get_secrets(k)
		mnem = to_phrase(interpolate(secrets, L))
		print("Your mnemonic is\n{}".format(mnem))
		

	def quit(self):
		sys.exit(0)

def to_phrase(num):
	return " ".join(ENG.get_word(n) for n in elev_bit_stream(num))

def elev_bit_stream(num):
	mask = (1 << 11) - 1
	while num:
		yield num & mask
		num = num >> 11

def get_mnem_length():
	l = int(input("What is the length of your mnemonic? "))
	return l

def get_threshold():
	return int(input("Threshold value: "))

def get_no_secrets():
	return int(input("How many secrets? "))

def get_phrase():
	phrase = input("Type your mnemonic phrase: ")
	return Phrase(phrase)

def share_secret(k, n, mnem):
	poly = Polynomial(k, n, mnem)
	print("Secret # | Phrase")
	for s in poly.secrets():
		print("{0}          {1}\n".format(s[0], to_phrase(s[1])))

def get_secrets(thresh):
	secrets = [None] * thresh
	for i in range(thresh):
		x = int(input("Secret # "))
		phrase = Phrase(input("Phrase: "))
		y = int(phrase)
		secrets[i] = (x, y)
	return secrets


if __name__ == "__main__":
	Menu().run()
