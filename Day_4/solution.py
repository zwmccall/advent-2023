import re
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = (os.path.join(__location__, 'input.txt'))
with open(input_path, "r") as input_file:
	games = input_file.readlines()

def build_array():
	games_array = []
	for game in games:
		game_array = []
		numbers = game.split('|')
		winning_nums = numbers[0]
		winning_nums = winning_nums[winning_nums.index(':')+1:]
		winning_nums = re.findall(r'\d+', winning_nums)
		game_array.append(winning_nums)
		game_nums = numbers[1]
		game_nums = re.findall(r'\d+', game_nums)
		game_array.append(game_nums)
		games_array.append(game_array)
	return games_array

def score_card(card, method):
	if method == 'points':
		score = 0
		for game_num in card[1]:
			if game_num in card[0]:
				if score == 0:
					score = 1
				else:
					score = score * 2
		return score

def part_1():
	sum = 0
	games_array = build_array()
	for game in games_array:
		sum += score_card(game, 'points')
	return str(sum)

def part_2():
	sum = 0
	games_array = build_array()
	return str(sum)

print('Part 1: ' + part_1())
print('Part 2: ' + part_2())

input_file.close()