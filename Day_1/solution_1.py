import re

input_file = open("Day_1/input.txt", "r")

sum = 0
for line in input_file:
	numbers = re.findall(r'\d', line)
	digits = numbers[0] + numbers[-1]
	sum += int(digits)
print(sum)

input_file.close()