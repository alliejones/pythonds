from enum import IntEnum
from enum import Enum

class CardSuit(Enum):
	hearts = 1
	clubs = 2
	spades = 3
	diamonds = 4

	def __str__(self):
		return self.name


class CardRank(IntEnum):
	ace = 14
	king = 13
	queen = 12
	jack = 11
	ten = 10
	nine = 9
	eight = 8
	seven = 7
	six = 6
	five = 5
	four = 4
	three = 3
	two = 2

	def __str__(self):
		return self.name
		

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return str(self.rank)+' of '+str(self.suit)

	def __eq__(self, other):
		return self.rank == other.rank

	def __gt__(self, other):
		return self.rank > other.rank

	def __lt__(self, other):
		return self.rank < other.rank
