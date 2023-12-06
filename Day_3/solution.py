import re

with open("Day_3/example_1.txt", "r") as input_file:
	lines = input_file.readlines()

def part_1():
	array = []
	for line in lines:
		x = list(line.strip())
		array.append(x)
	print(array)
	for idx, line in enumerate(array):
		mid_digit = False
		temp_array = []
		for jdx, element in enumerate(line):
			if element.isdigit():
				temp_array.append([idx,jdx])
				if mid_digit:
					array[idx][jdx] = '.'
				if not idx == 0:
					if not jdx == 0:
						if not array[idx-1][jdx-1].isdigit() and not array[idx-1][jdx-1] == '.':
							array[idx][jdx] = '.'
							mid_digit = True
							for i in temp_array: array[i[0]][i[1]] = '.'
					if not array[idx-1][jdx].isdigit() and not array[idx-1][jdx] == '.':
						array[idx][jdx] = '.'
						mid_digit = True
						for i in temp_array: array[i[0]][i[1]] = '.'
					if not jdx == len(line) - 1:
						if not array[idx-1][jdx+1].isdigit() and not array[idx-1][jdx+1] == '.':
							array[idx][jdx] = '.'
							mid_digit = True
							for i in temp_array: array[i[0]][i[1]] = '.'
				if not jdx == 0:
					if not array[idx][jdx-1].isdigit() and not array[idx][jdx-1] == '.':
						array[idx][jdx] = '.'
						mid_digit = True
						for i in temp_array: array[i[0]][i[1]] = '.'
				if not jdx == len(line) - 1:
					if not array[idx][jdx+1].isdigit() and not array[idx][jdx+1] == '.':
						array[idx][jdx] = '.'
						mid_digit = True
						for i in temp_array: array[i[0]][i[1]] = '.'
				if not idx == len(array) - 1:
					if not jdx == 0:
						if not array[idx+1][jdx-1].isdigit() and not array[idx+1][jdx-1] == '.':
							array[idx][jdx] = '.'
							mid_digit = True
							for i in temp_array: array[i[0]][i[1]] = '.'
					if not array[idx-1][jdx].isdigit() and not array[idx-1][jdx] == '.':
						array[idx][jdx] = '.'
						mid_digit = True
						for i in temp_array: array[i[0]][i[1]] = '.'
					if not jdx == len(line) - 1:
						if not array[idx+1][jdx+1].isdigit() and not array[idx+1][jdx+1] == '.':
							print(temp_array[0][1])
							array[idx][jdx] = '.'
							mid_digit = True
							for i in temp_array: array[i[0]][i[1]] = '.'
			else:
				mid_digit = False
				temp_array = []
			#print(idx, jdx)
	return str(array)

print('Part 1: ' + part_1())

input_file.close()