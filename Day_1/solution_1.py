import re

input = open("Day_1/input.txt", "r")

sum = 0;
digits = ''
for line in input:
	numbers = re.findall(r'\d', line)
	digits = numbers[0] + numbers[len(numbers)-1]
	sum += int(digits)
print(sum)

input.close()