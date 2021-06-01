import re

class FileHandlerStory():
	'''Структура файла в группах слайдах по несколько страничек
	страничка - список
	группа - тоже список (уровень +1)
	все истории в словаре по ключам-названиям'''
	def __init__(self, filename):
		self.filename = filename
		self.stories = {}
		story = []  # собрание страничек
		undstory = []  # страничка
		self.pics = []  # список картинок для загрузки
		with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				line = line.strip()
				if line[0] == '*':
					name = line[1:]
					# name = re.findall(r"'(.*?)'", line)
					story = []
				elif line[0] == '@':
					self.stories[name] = story
				elif line[0] == '-':
					undstory = []
				elif line[0] == '+':
					story.append(undstory)
				elif line[0] == '^':  # картинка координаты наклеить куда
					pict_name = re.findall(r"'(.*?)'", line)[0]
					pict_x = int(re.findall(r'\d+', line)[0])
					pict_y = int(re.findall(r'\d+', line)[1])
					undstory.append((pict_name, pict_x, pict_y))
					self.pics.append(pict_name)
				else:
					undstory.append(line)

		# print(self.stories)
	# def create_one_story(self, name):
	# 	pre_story = self.stories[name]
	# 	for ps in pre_story:
	# 		if ps[0] == '^':









# class FileHandler():
# 	def __init__(self, filename):
# 		self.filename = filename
# 		self.file_score = 0

# 	def write_to_file(self, coins, score):
# 		if self.file_score > score:
# 			score = self.file_score
# 			coins += self.file_coins
# 		with open(self.filename, 'a') as f:
# 			f.write('coins' + str(coins))
# 			f.write('score' + str(score))

# 	def read_from_file(self):
# 		coins = 0
# 		with open(file_name, 'r') as f:
# 			for line in f[-2]:  # нужна будет последняя строка с конца
# 				if line.startwith('coins'):
# 					score = line[6:]

# 		best_score = 0
# 		with open(file_name, 'r') as f:
# 			for line in f[-1]:  # нужна будет последняя строка с конца
# 				if line.startwith('score'):
# 					best_score = line[6:]

# 		self.file_score = best_score
# 		self.file_coins = coins

# 		return coins, best_score


# Устройство файла: 
# coins 10
# score 10000

		
