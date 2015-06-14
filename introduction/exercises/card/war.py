# implementing these rules: http://www.pagat.com/war/war.html#two
import random

from card import Card, CardSuit, CardRank
from deck import Deck

class WarRunner:
	def __init__(self, print_to_console = True):
		cards = self.create_cards()
		half = len(cards) // 2
		
		p1_deck = Deck(cards[0:half])
		p2_deck = Deck(cards[half:])

		self.game = WarGame(p1_deck, p2_deck, print_to_console)

	def create_cards(self):
		cards = []
		for suit in CardSuit:
			for rank in CardRank:
				cards.append(Card(suit, rank))

		random.shuffle(cards)
		return cards

	def play(self):
		while not self.game.game_over():
			self.game.turn()
			if self.game.turn_count >= 5000:
				break

		return self.game.end()

class WarGame:
	def __init__(self, p1_deck, p2_deck, print_to_console = True):
		self.p1_deck = p1_deck
		self.p2_deck = p2_deck

		self.turn_count = 0
		self.war_count = 0
		self.war_depths = []

		self.print_to_console =	print_to_console

	def display(self, str):
		if self.print_to_console:
			print(str) 

	def turn(self):
		self.turn_count += 1

		p1_card = self.p1_deck.draw()
		self.display('Player one draws '+str(p1_card))
		p2_card = self.p2_deck.draw()
		self.display('Player two draws '+str(p2_card))

		if p1_card == p2_card:
			self.display('WAR!')
			self.war_count += 1
			self.do_war([ p1_card ], [ p2_card ])
		elif p1_card > p2_card:
			self.display('Player one takes the cards')
			self.p1_deck.add_to_bottom([ p1_card, p2_card ])
		else:
			self.display('Player two takes the cards')
			self.p2_deck.add_to_bottom([ p1_card, p2_card ])

		self.display('Score: P1 {} | P2 {}\n'.format(self.p1_deck.size(), self.p2_deck.size()))

	# war is recursive!
	def do_war(self, p1_cards, p2_cards, depth = 1):
		# implemented rule: whoever runs out of cards
		# during a war first loses
		
		if self.game_over():
			self.display(self.no_cards_message())
			return

		p1_hidden = self.p1_deck.draw()
		self.display('Player one draws a hidden card')
		p2_hidden = self.p2_deck.draw()
		self.display('Player two draws a hidden card')

		if self.game_over():
			self.display(self.no_cards_message())
			return

		p1_shown = self.p1_deck.draw()
		self.display('Player one draws '+str(p1_shown))
		p2_shown = self.p2_deck.draw()
		self.display('Player two draws '+str(p2_shown))

		if self.game_over():
			self.display(self.no_cards_message())
			return	

		if p1_shown == p2_shown:
			self.display('WAR (again)!')
			p1_cards.extend([ p1_hidden, p1_shown ])
			p2_cards.extend([ p2_hidden, p2_shown ])
			self.do_war(p1_cards, p2_cards, depth + 1)
		else:
			self.war_depths.append(depth)

			all_the_cards = p1_cards
			all_the_cards.extend(p2_cards)
			all_the_cards.extend([ p1_hidden, p1_shown, p2_hidden, p2_shown ])

			if p1_shown > p2_shown:
				self.display('Player one takes all {} cards'.format(len(all_the_cards)))
				self.p1_deck.add_to_bottom(all_the_cards)
			else:
				self.display('Player two takes all {} cards'.format(len(all_the_cards)))
				self.p2_deck.add_to_bottom(all_the_cards)

	def no_cards_message(self):
		if len(self.p1_deck) == 0 and len(self.p2_deck) == 0:
			return 'Both players run out of cards.'
		else:
			loser = 'one' if len(self.p1_deck) == 0 else 'two'
			return 'Player %s runs out of cards.' % loser

	def game_over(self):
		return len(self.p1_deck) == 0 or len(self.p2_deck) == 0

	def end(self):
		self.display("GAME OVER")

		if len(self.p1_deck) > len(self.p2_deck):
			winner = 'one'
			self.display('Player 1 wins!')
		elif len(self.p1_deck) < len(self.p2_deck):
			winner = 'two'
			self.display('Player 2 wins!')
		else:
			# this can only happen if both players run out of
			# cards simultaneously during a war
			winner = 'tie'
			self.display("It's a tie!")

		self.display('Some stats: this game lasted for %d turns and players warred %d times.' % (self.turn_count, self.war_count))

		return {
			'winner': winner,
			'turn_count': self.turn_count,
			'war_count': self.war_count,
			'war_depths': self.war_depths
		}

	def __str__(self):
		return 'Player 1 deck:\n'+str(self.p1_deck)+"\n\nPlayer 2 deck:\n"+str(self.p2_deck)
	


if __name__ == '__main__':
	game = WarRunner()
	game.play()
