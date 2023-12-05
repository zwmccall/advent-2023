import re

input = open("Day_1/input.txt", "r")

sum = 0;
digits = ''
digit_1 = ''
digit_2 = ''
units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in input:
	numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
	if numbers[0].isdigit():
		digit_1 = str(numbers[0])
	else:
		digit_1 = str(units.index(numbers[0]))

	if numbers[len(numbers)-1].isdigit():
		digit_2 = str(numbers[len(numbers)-1])
	else:
		digit_2 = str(units.index(numbers[len(numbers)-1]))
	digits = str(digit_1) + str(digit_2)
	sum += int(digits)
print(sum)

input.close()