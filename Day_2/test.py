import re

input_file = open("Day_2/example_1.txt", "r")

sum = 0
temp_sum = 0
for game in input_file:
	rounds = game.split(';')
	red_max = 0
	green_max = 0
	blue_max = 0
	for round in rounds:
		print(round)
		red_count = re.findall(r'\d+(?=\ red)', round)
		if not red_count: red_count = ['0']
		print(red_max)

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
print(str(sum))

input_file.close()