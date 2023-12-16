import re
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = (os.path.join(__location__, 'input.txt'))
with open(input_path, "r") as input_file:
	cards = input_file.readlines()

def build_array():
	cards_array = []
	for card in cards:
		card_array = []
		numbers = card.split('|')
		winning_nums = numbers[0]
		winning_nums = winning_nums[winning_nums.index(':')+1:]
		winning_nums = re.findall(r'\d+', winning_nums)
		card_array.append(winning_nums)
		card_nums = numbers[1]
		card_nums = re.findall(r'\d+', card_nums)
		card_array.append(card_nums)
		card_array.append(1)
		cards_array.append(card_array)
	return cards_array

def score_card(card, method):
	score = 0
	if method == 'points':
		for num in card[1]:
			if num in card[0]:
				if score == 0:
					score = 1
				else:
					score = score * 2
		return score
	elif method == 'cards':
		for num in card[1]:
			if num in card[0]:
				score += 1
		return score

def part_1():
	sum = 0
	cards_array = build_array()
	for card in cards_array:
		sum += score_card(card, 'points')
	return str(sum)

def part_2():
	sum = 0
	cards_array = build_array()
	for idx, card in enumerate(cards_array):
		# Find matches for each copy of the card
		for _ in range(0,card[2]):
			matches = score_card(card, 'cards')
			# For x num of matches increment the number of the next x cards
			for match in range(1,matches+1):
				cards_array[idx+match][2] += 1
	# sum up the num copies of each card
	for card in cards_array:
		sum += int(card[2])
	return str(sum)

print('Part 1: ' + part_1())
print('Part 2: ' + part_2())

input_file.close()