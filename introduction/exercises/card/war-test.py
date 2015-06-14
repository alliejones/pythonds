import unittest

from war import WarGame
from card import Card, CardSuit as Suit, CardRank as Rank
from deck import Deck

class WarTest(unittest.TestCase):
	# test when players play cards of the same value
	def test_war(self):
		p1_cards = [
			Card(Suit.diamonds, Rank.king),
			Card(Suit.spades, Rank.two),
			Card(Suit.diamonds, Rank.ten), # value match
			Card(Suit.diamonds, Rank.four),
			Card(Suit.diamonds, Rank.five), # match
			Card(Suit.diamonds, Rank.six),
			Card(Suit.diamonds, Rank.seven)
		]
		p2_cards = [
			Card(Suit.clubs, Rank.king),
			Card(Suit.clubs, Rank.five),
			Card(Suit.hearts, Rank.ten), # value match
			Card(Suit.hearts, Rank.nine),
			Card(Suit.hearts, Rank.five), # match
			Card(Suit.hearts, Rank.seven),
			Card(Suit.hearts, Rank.six)

		]
		game = WarGame(Deck(p1_cards), Deck(p2_cards))
		game.turn()

		self.assertEqual(game.p1_deck.size(), 14)
		self.assertEqual(game.p2_deck.size(), 0)


if __name__ == '__main__':
    unittest.main()