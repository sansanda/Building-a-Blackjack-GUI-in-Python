import unittest
import sys
from io import StringIO
from Logic.Card import Card
from Logic.Hand import Hand

class UnitTests(unittest.TestCase):

    def test_hand_value4(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Spades", "9"))
        playersHand.add_card(Card("Hearts", "9"))
        playersHand.add_card(Card("Diamonds", "9"))
        self.assertEqual(27, playersHand.get_value())

    def test_hand_value3(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Spades", "2"))
        playersHand.add_card(Card("Hearts", "2"))
        playersHand.add_card(Card("Diamonds", "2"))
        playersHand.add_card(Card("Clubs", "2"))
        self.assertEqual(8, playersHand.get_value())

    def test_hand_value2(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "K"))
        playersHand.add_card(Card("Hearts", "J"))
        self.assertEqual(20, playersHand.get_value())

    def test_hand_value1(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "K"))
        playersHand.add_card(Card("Hearts", "3"))
        self.assertEqual(13, playersHand.get_value())

    def test_hand_ace5(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "A"))
        playersHand.add_card(Card("Diamonds", "A"))
        self.assertEqual(12, playersHand.get_value())


    def test_hand_ace4(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "A"))
        playersHand.add_card(Card("Spades", "2"))
        self.assertEqual(13, playersHand.get_value())

    def test_hand_ace3(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "K"))
        playersHand.add_card(Card("Spades", "5"))
        playersHand.add_card(Card("Clubs", "A"))
        self.assertEqual(16, playersHand.get_value())

    def test_hand_ace2(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "K"))
        playersHand.add_card(Card("Hearts", "A"))
        self.assertEqual(21, playersHand.get_value())

    def test_hand_ace1(self):
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "K"))
        playersHand.add_card(Card("Spades", "K"))
        playersHand.add_card(Card("Clubs", "A"))
        self.assertEqual(21, playersHand.get_value())

    def test_hand_isPlayer1(self):
        out = StringIO()
        sys.stdout = out
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Clubs", "King"))
        playersHand.add_card(Card("Hearts", "A"))
        playersHand.display()
        output = out.getvalue().strip()
        self.assertIn("King of Clubs", output)
        self.assertIn("A of Hearts", output)
        self.assertNotIn("hidden", output)

    def test_hand_isPlayer2(self):
        out = StringIO()
        sys.stdout = out
        playersHand = Hand(dealer=False)
        playersHand.add_card(Card("Spades", "8"))
        playersHand.add_card(Card("Diamonds", "2"))
        playersHand.add_card(Card("Diamonds", "10"))
        playersHand.display()
        output = out.getvalue().strip()
        self.assertIn("8 of Spades", output)
        self.assertIn("2 of Diamonds", output)
        self.assertIn("10 of Diamonds", output)
        self.assertNotIn("hidden", output)

    def test_hand_isDealer1(self):
        out = StringIO()
        sys.stdout = out
        dealersHand = Hand(dealer=True)
        dealersHand.add_card(Card("Spades", "8"))
        dealersHand.add_card(Card("Diamonds", "2"))
        dealersHand.display()
        output = out.getvalue().strip()
        self.assertIn("hidden", output)
        self.assertNotIn("8 of Spades", output)

    def test_hand_isDealer2(self):
        out = StringIO()
        sys.stdout = out
        dealersHand = Hand(dealer=True)
        dealersHand.add_card(Card("Clubs", "K"))
        dealersHand.add_card(Card("Hearts", "A"))
        dealersHand.display()
        output = out.getvalue().strip()
        self.assertIn("hidden", output)
        self.assertNotIn("K of Clubs", output)