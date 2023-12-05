import re

input_file = open("Day_1/input.txt", "r")

sum = 0
units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in input_file:
	numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

	digit_1 = str(numbers[0]) if numbers[0].isdigit() else str(units.index(numbers[0]))
	digit_2 = str(numbers[-1]) if numbers[-1].isdigit() else str(units.index(numbers[-1]))

	digits = digit_1 + digit_2
	sum += int(digits)
print(sum)

input_file.close()