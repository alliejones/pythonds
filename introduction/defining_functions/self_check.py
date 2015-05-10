import string
import random

letters = [char for char in string.ascii_lowercase] 
letters.append(' ')

goal_string = "methinks it is like a weasel"

# Write a function that generates a string that is 27 
# characters long by choosing random letters from the 26 
# letters in the alphabet plus the space.

def random_string():
	return ''.join([letters[random.randint(0, len(letters) - 1)] for i in range(0, len(goal_string))])

# Write another function that will score each generated
# string by comparing the randomly generated string to the goal.

def score_string(str):
	score = 0
	for i, c in enumerate(goal_string):
		if c == str[i]:
			score += 1
	return score

# A third function will repeatedly call generate and score, 
# then if 100% of the letters are correct we are done. If the 
# letters are not correct then we will generate a whole new 
# string.
# To make it easier to follow your program's progress this 
# third function should print out the best string generated so 
# far and its score every 1000 tries.

def generate():
	curr_string = ''
	i = 0

	while curr_string != goal_string:
		curr_string = random_string()
		i += 1
		if i % 1000 == 0:
			print(curr_string, score_string(curr_string))

	print('Total iterations:', i)


generate()