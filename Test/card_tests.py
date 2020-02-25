import unittest
import sys
from io import StringIO
from Logic.Card import Card


class UnitTests(unittest.TestCase):

    def test_card_initialization(self):
        try:
            card = Card("Spades", "8")
        except:
            self.fail("Unable to initialize a 'Card' object, exception thrown")

    def test_card_printation(self):

        out = StringIO()
        sys.stdout = out

        card1 = Card('Spades', '8')
        print(card1)
        output = out.getvalue().strip()
        ps1 = "8 of Spades"
        self.assertEqual(output, ps1)
        out.truncate(0)
        out.seek(0)

        card2 = Card('Diamonds', 'King')
        print(card2)
        output = out.getvalue().strip()
        ps2 = "King of Diamonds"
        self.assertEqual(output, ps2)
        out.truncate(0)
        out.seek(0)

        card3 = Card('Hearts', 'Ace')
        print(card3)
        output = out.getvalue().strip()
        ps3 = "Ace of Hearts"
        self.assertEqual(output, ps3)
        out.truncate(0)
        out.seek(0)

        card4 = Card('Clubs', '5')
        print(card4)
        output = out.getvalue().strip()
        ps4 = "5 of Clubs"
        self.assertEqual(output, ps4)
        out.close

