import string
import random

letters = [char for char in string.ascii_lowercase] 
letters.append(' ')

goal_string = "methinks it is like a weasel"

# Write a function that generates a string that is 27 
# characters long by choosing random letters from the 26 
# letters in the alphabet plus the space.

def random_letter():
	return letters[random.randint(0, len(letters) - 1)]

def random_string():
	return ''.join([random_letter() for i in range(0, len(goal_string))])

# Write another function that will score each generated
# string by comparing the randomly generated string to the goal.

def score_string(str):
	score = 0

	for i, c in enumerate(goal_string):
		if c == str[i]:
			score += 1
			
	return score

def index_to_change(str):
	i = 0
	while str[i] == goal_string[i]:
		i += 1
	return i

# Improve upon the program in the self check by keeping letters
# that are correct and only modifying one character in the best 
# string so far.

def change_letter(str, i):
	return str[:i] + random_letter() + str[i + 1:]

def generate():
	str = random_string()
	i = 0

	while str != goal_string:
		str = change_letter(str, index_to_change(str))
		print(str, score_string(str))
		i += 1

	print('Iterations:', i)

generate()