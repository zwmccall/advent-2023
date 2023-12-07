import re

with open("Day_3/input.txt", "r") as input_file:
	lines = input_file.readlines()

def part_1():
	array = []
	for line in lines:
		x = list(line.strip())
		array.append(x)
	for idx, line in enumerate(array):
		is_partnum = False
		temp_array = []
		for jdx, element in enumerate(line):
			if element.isdigit():
				temp_array.append([idx,jdx])
				if not idx == 0:
					if not jdx == 0:
						if not array[idx-1][jdx-1].isdigit() and not array[idx-1][jdx-1] == '.':
							is_partnum = True
					if not array[idx-1][jdx].isdigit() and not array[idx-1][jdx] == '.':
						is_partnum = True
					if not jdx == len(line) - 1:
						if not array[idx-1][jdx+1].isdigit() and not array[idx-1][jdx+1] == '.':
							is_partnum = True
				if not jdx == 0:
					if not array[idx][jdx-1].isdigit() and not array[idx][jdx-1] == '.':
						is_partnum = True
				if not jdx == len(line) - 1:
					if not array[idx][jdx+1].isdigit() and not array[idx][jdx+1] == '.':
						is_partnum = True
				if not idx == len(array) - 1:
					if not jdx == 0:
						if not array[idx+1][jdx-1].isdigit() and not array[idx+1][jdx-1] == '.':
							is_partnum = True
					if not array[idx+1][jdx].isdigit() and not array[idx+1][jdx] == '.':
						is_partnum = True
					if not jdx == len(line) - 1:
						if not array[idx+1][jdx+1].isdigit() and not array[idx+1][jdx+1] == '.':
							is_partnum = True
			else:
				if not is_partnum:
					for num_indexes in temp_array: array[num_indexes[0]][num_indexes[1]] = '.'
				is_partnum = False
				temp_array = []
		if not is_partnum:
			for num_indexes in temp_array: array[num_indexes[0]][num_indexes[1]] = '.'

	new = "" 

	# traverse in the string 
	for row in array:
		for char in row:
			new += char 
	numbers = re.findall(r'\d+', new)
	sum = 0
	for number in numbers:
		sum += int(number)
	
	return str(sum)

print('Part 1: ' + part_1())

input_file.close()