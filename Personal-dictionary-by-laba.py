#this software is a copyrighted product made by laba.not for resell. all right reserved.date-7th may 2018. one of the 1st software made by laba.

print("Welcome to Personal dictionary by laba.\nThis ugliest software is made by most handsome man alive name laba.")
print("\nThis software aims to make your process for learning new words easy. \nJust add a new word and a note describing it. Revice twice a day.")
words = []
notes = []

def word_entry(word):
	w_entry = {"word": word}
	words.append(w_entry)
	

def note_entry(note):
	n_entry = {"note": note}
	notes.append(n_entry)


def inputf():
	word_input = input("Enter the word you wanna add: ")
	note_input = input("Enter description note: ")
	word_entry(word_input)
	note_entry(note_input)
	save_file(word_input, note_input)


def save_file(word, note):
	try:
		f = open("log.txt", "a")
		f.write(word + " - " + note + "\n")
		f.close()
	except Exception:
		print("uh oh! fucked up while saving \ntrying to unfuck...")	


def read_file():
	try:
		f = open("log.txt", "r")
		print("\nWORD - NOTE\n")		
		"""generator function"""
		def read_lines(f):
			for line in f:
				yield line

		
		for entry in read_lines(f):
			print(entry)
		f.close()			
	except Exception:
		ask = input("\nHey niggah, how are you doin? using this software for 1st time? \nDon't worry its easy to use. \nTo add a new word in your personal dictionary Type Y ;-D - ")
		if (ask == "Y"):
			inputf()
			print("see its easy!!")
		else:
			print("capital Y niggah ;-|")


read_file()

num = 1
while (num == 1):
	ask_again = input("Wanna add more word? type Y for yes, N for exit - ")
	if ask_again == "Y":
		inputf()
		continue
	elif ask_again == "y":
		print("fucking fuuuuuck... are you fuckin blind? or trying to break my software ? can't read a simple instruction? type CAPITAL Y.")		
	else:
		break