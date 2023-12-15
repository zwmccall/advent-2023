# Script to setup files and folders for each day of Advent of Code
import os
import requests
from bs4 import BeautifulSoup
import datetime
import constants

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Creates folder for the day if one doesn't exist
def create_folder(num_day):
	folder_path = (os.path.join(__location__, f"..\Day_{num_day}"))
	try:
		# Check if the folder does not exist
		if not os.path.exists(folder_path):
			# Create the folder
			os.makedirs(folder_path)
			print(f"Folder '{folder_path}' created successfully.")
		else:
			print(f"Folder '{folder_path}' already exists.")
	except Exception as e:
		print(f"Error creating folder '{folder_path}': {str(e)}")

# Downloads the day's input file if it doesn't exist
def download_input(num_day):
	try:
		file_path = (os.path.join(__location__, f"..\Day_{num_day}\input.txt"))
		if not os.path.exists(file_path):
			url = f"https://adventofcode.com/2023/day/{num_day}/input"
			headers = {
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
			}
			cookies = {
				"session": constants.SESSION_COOKIE
			}

			response = requests.get(url, headers=headers, cookies=cookies)

			# Check if the request was successful (status code 200)
			if response.status_code == 200:
				# Parse the HTML content
				results = BeautifulSoup(response.text, 'html.parser')

				# Get the text content
				text_content = results.get_text()

				# Save the text content to a file
				with open(file_path, 'w', encoding='utf-8') as file:
					file.write(text_content)

				print(f"Day {num_day} input data downloaded successfully.")
			else:
				print(f"Error: Unable to fetch the website. Status code: {response.status_code}")
		else:
			print(f"Day {num_day} input data already exists.")
	except Exception as e:
		print(f"Error: {str(e)}")

# Downloads the puzzle info, can run again after finishing part 1 to add part 2 puzzle info
def download_puzzle(num_day):
	try:
		url = f"https://adventofcode.com/2023/day/{num_day}"
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
		}
		cookies = {
			"session": constants.SESSION_COOKIE
		}

		response = requests.get(url, headers=headers, cookies=cookies)

		# Check if the request was successful (status code 200)
		if response.status_code == 200:
			# Parse the HTML content
			results = BeautifulSoup(response.text, 'html.parser')

			# Get the text content
			content = results.find_all("article", class_="day-desc")

			text_content = content[0].get_text()
			if len(content) == 2:
				text_content = content[0].get_text() + '\n' + content[1].get_text()

			# Save the text content to a file
			file_path = (os.path.join(__location__, f"..\Day_{num_day}\puzzle.txt"))
			with open(file_path, 'w', encoding='utf-8') as file:
				file.write(text_content)

			print("Puzzle info downloaded successfully.")

			# Get the text content
			examples = results.find_all("pre")

			for idx, example in enumerate(examples):
				text_content = example.text.strip()
				# Save the text content to a file
				file_path = (os.path.join(__location__, f"..\Day_{num_day}\example_{idx+1}.txt"))
				with open(file_path, 'w', encoding='utf-8') as file:
					file.write(text_content)

				print(f"Example {idx+1} downloaded successfully.")

		else:
			print(f"Error: Unable to fetch the website. Status code: {response.status_code}")
	except Exception as e:
		print(f"Error: {str(e)}")

# Creates solution file from boilerplate
def create_solution(num_day):
	folder_path = (os.path.join(__location__, f"..\Day_{num_day}"))
	try:
		# Check if the folder does not exist
		if not os.path.exists(folder_path):
			# Create the folder
			os.makedirs(folder_path)
			print(f"Folder '{folder_path}' created successfully.")
		else:
			print(f"Folder '{folder_path}' already exists.")
	except Exception as e:
		print(f"Error creating folder '{folder_path}': {str(e)}")

# Valid day is between 1-31 and only dates that have already been unlocked
def get_valid_day(prompt):
	while True:
		try:
			value = int(input(prompt))
		except ValueError:
			print("Sorry, I didn't understand that.")
			continue

		if value < 1:
			print("Sorry, your response must be greater than zero.")
			continue
		if value > 31:
			print("Sorry, your response must be less than thirty-one.")
			continue
		if str(datetime.datetime.now()) < '2024-01-01':
			if value > datetime.datetime.now().day:
				print("Sorry, that date is not available yet.")
				continue
			else:
				break
		else:
			break
	return value

num_day = get_valid_day("Enter the number day: ")

create_folder(num_day)
download_input(num_day)
download_puzzle(num_day)