import random
# Probably overkill for these small lists, but hey
# (also appropriate name right?)
from collections import deque

class Deck:
	def __init__(self, cards):
		# first (left) element = top of deck
		self.cards = deque(cards)

	def size(self):
		return len(self.cards)

	def draw(self):
		return self.cards.popleft()

	def add_to_bottom(self, cards):
		# random.shuffle(cards)
		self.cards.extend(cards)

	def __str__(self):
		return ', '.join([str(card) for card in self.cards])

	def __len__(self):
		return self.size()