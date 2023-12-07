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
					if not array[idx-1][jdx].isdigit() and not array[idx-1][jdx] == '.':
						is_partnum = True
					if not jdx == len(line) - 1:
						if not array[idx+1][jdx+1].isdigit() and not array[idx+1][jdx+1] == '.':
							is_partnum = True
			else:
				if not is_partnum:
					for i in temp_array: array[i[0]][i[1]] = '.'
				is_partnum = False
				temp_array = []
			#print(idx, jdx)
	return str(array)

print('Part 1: ' + part_1())

input_file.close()