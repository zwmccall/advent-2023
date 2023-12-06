import re

with open("Day_2/input.txt", "r") as input_file:
	games = input_file.readlines()

def part_1():
	sum = 0
	for game in games:
		id = re.findall(r'\d+(?=\:)', game)
		rounds = game.split(';')
		possible = True
		for round in rounds:
			red_count = re.findall(r'\d+(?=\ red)', round)
			if not red_count: red_count = ['0']
			if int(red_count[0]) > 12:
				possible = False
				break
			green_count = re.findall(r'\d+(?=\ green)', round)
			if not green_count: green_count = ['0']
			if int(green_count[0]) > 13:
				possible = False
				break
			blue_count = re.findall(r'\d+(?=\ blue)', round)
			if not blue_count: blue_count = ['0']
			if int(blue_count[0]) > 14:
				possible = False
				break
		if possible == True:
			sum += int(id[0])
	return str(sum)

def part_2():
	sum = 0
	temp_sum = 0
	for game in games:
		rounds = game.split(';')
		red_max = 0
		green_max = 0
		blue_max = 0
		for round in rounds:
			red_count = re.findall(r'\d+(?=\ red)', round)
			if not red_count: red_count = ['0']
			if int(red_count[0]) > red_max:
				red_max = int(red_count[0])
			green_count = re.findall(r'\d+(?=\ green)', round)
			if not green_count: green_count = ['0']
			if int(green_count[0]) > green_max:
				green_max = int(green_count[0])
			blue_count = re.findall(r'\d+(?=\ blue)', round)
			if not blue_count: blue_count = ['0']
			if int(blue_count[0]) > blue_max:
				blue_max = int(blue_count[0])
			temp_sum = red_max * green_max * blue_max
		sum += temp_sum
	return str(sum)

print('Part 1: ' + part_1())
print('Part 2: ' + part_2())

input_file.close()