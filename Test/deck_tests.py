import unittest
from Logic.Deck import Deck

class UnitTests(unittest.TestCase):

    def test_deck_dealHalf(self):
        deck = Deck()
        for i in range(1, 38):
            deck.deal()
        self.assertEqual(len(deck.cards), 15)

    def test_deck_deal(self):
        deck = Deck()
        deck.deal()
        self.assertEqual(len(deck.cards), 51)
