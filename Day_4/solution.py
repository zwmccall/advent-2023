import re
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = (os.path.join(__location__, 'input.txt'))
with open(input_path, "r") as input_file:
	cards = input_file.readlines()

def build_array():
	all_cards_array = []
	for card in cards:
		winning_nums = re.findall(r'\d+', card.split('|')[0].split(':')[1])
		card_nums = re.findall(r'\d+', card.split('|')[1])

		all_cards_array.append([winning_nums, card_nums, 1])
	return all_cards_array

def score_card(card, method):
	matches = sum(1 for num in card[1] if num in card[0])

	if method == 'points':
		score = 0 if matches == 0 else 2**(matches - 1)
		return score
	elif method == 'cards':
		return matches

def part_1(all_cards_array):
	total_sum = sum(score_card(card, 'points') for card in all_cards_array)
	return str(total_sum)

def part_2(all_cards_array):
	for cur_idx, card in enumerate(all_cards_array):
		# Find matches for each copy of the card
		for _ in range(0,card[2]):
			matches = score_card(card, 'cards')
			# For x num of matches increment the number of the next x cards
			for match_idx in range(1,matches+1):
				all_cards_array[cur_idx+match_idx][2] += 1
	# sum up the num copies of each card
	total_sum = sum(int(card[2]) for card in all_cards_array)
	return str(total_sum)

all_cards_array = build_array()
print('Part 1: ' + part_1(all_cards_array))
print('Part 2: ' + part_2(all_cards_array))

input_file.close()