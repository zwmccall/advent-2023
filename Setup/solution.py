import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = (os.path.join(__location__, 'input.txt'))
with open(input_path, "r") as input_file:
	games = input_file.readlines()

def part_1():
	return 'Part 1 boilerplate'

def part_2():
	return 'Part 2 boilerplate'

print('Part 1: ' + part_1())
print('Part 2: ' + part_2())

input_file.close()