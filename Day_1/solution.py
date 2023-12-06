import re

with open("Day_1/input.txt", "r") as input_file:
	lines = input_file.readlines()

def part_1():
	sum = 0
	for line in lines:
		numbers = re.findall(r'\d', line)
		digits = numbers[0] + numbers[-1]
		sum += int(digits)
	return str(sum)

def part_2():
	sum = 0
	units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

	for line in lines:
		numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

		digit_1 = str(numbers[0]) if numbers[0].isdigit() else str(units.index(numbers[0]))
		digit_2 = str(numbers[-1]) if numbers[-1].isdigit() else str(units.index(numbers[-1]))

		digits = digit_1 + digit_2
		sum += int(digits)
	return str(sum)
	
print('Part 1: ' + part_1())
print('Part 2: ' + part_2())

input_file.close()