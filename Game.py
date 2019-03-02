import os
import random

def read_file(filename):
	list_words = []
	f = open(filename, "r")
	for word in f:
		list_words.append(word.strip())
	return list_words

def shuffle_word(word):
	return ''.join(random.sample(word,len(word)))

def game(level):
	score = 0
	i 	= 0

	list_words = read_file('Words' + str(level) + '.txt')
	random_num = random.sample(range(len(list_words)), len(list_words))
	os.system('cls' if os.name == 'nt' else 'clear')
	print('-------')
	print('LEVEL ' + str(level))
	print('-------')
	while (i < len(list_words)):
		print('Tebak kata: ' + shuffle_word(list_words[random_num[i]]))
		is_answer_right = False
		while (not is_answer_right):
			tebakan = input('Jawab: ')
			if (tebakan == list_words[random_num[i]]):
				score += 1
				i += 1
				is_answer_right = True
				print('BENAR! point anda ' + str(score))
			else:
				print('SALAH! silahkan coba lagi')
	print('----------------------------------------')
	print('Selamat Anda telah menyelesaikan level ' + str(level))
	print('----------------------------------------')

level = 1
MAX_LEVEL = 2

os.system('cls' if os.name == 'nt' else 'clear')
print('Selamat Bermain\n')
while (level <= MAX_LEVEL):
	game(level)
	level += 1
