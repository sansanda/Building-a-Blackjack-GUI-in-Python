import unittest
import sys
from io import StringIO
from Logic.Card import Card
from Logic.Hand import Hand
from Logic.Game import Game


class UnitTests(unittest.TestCase):

    def test_blackjack_check2(self):
        game = Game()
        game.dealer_hand = Hand(dealer=True)
        game.dealer_hand.add_card(Card("Spades", "2"))
        game.dealer_hand.add_card(Card("Spades", "J"))
        game.player_hand = Hand(dealer=False)
        game.player_hand.add_card(Card("Clubs", "A"))
        game.player_hand.add_card(Card("Hearts", "Q"))
        player, dealer = game.check_for_blackjack()
        print(dealer)
        print(player)
        self.assertFalse(dealer)
        self.assertTrue(player)

    def test_blackjack_check3(self):
        game = Game()
        game.dealer_hand = Hand(dealer=True)
        game.dealer_hand.add_card(Card("Spades", "A"))
        game.dealer_hand.add_card(Card("Spades", "J"))
        game.player_hand = Hand(dealer=False)
        game.player_hand.add_card(Card("Clubs", "A"))
        game.player_hand.add_card(Card("Hearts", "K"))
        player, dealer = game.check_for_blackjack()
        print(dealer)
        print(player)
        self.assertTrue(dealer)
        self.assertTrue(player)

    def test_blackjack_check1(self):
        game = Game()
        game.dealer_hand = Hand(dealer=True)
        game.dealer_hand.add_card(Card("Spades", "A"))
        game.dealer_hand.add_card(Card("Spades", "J"))
        game.player_hand = Hand(dealer=False)
        game.player_hand.add_card(Card("Clubs", "K"))
        game.player_hand.add_card(Card("Hearts", "3"))
        player, dealer = game.check_for_blackjack()
        print(dealer)
        print(player)
        self.assertTrue(dealer)
        self.assertFalse(player)

    def test_blackjack_results1(self):
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.dealer_hand = Hand(dealer=True)
        game.dealer_hand.add_card(Card("Spades", "A"))
        game.dealer_hand.add_card(Card("Spades", "J"))
        game.player_hand = Hand(dealer=False)
        game.player_hand.add_card(Card("Clubs", "A"))
        game.player_hand.add_card(Card("Hearts", "J"))
        player, dealer = game.check_for_blackjack()
        game.show_blackjack_results(player, dealer)
        output = out.getvalue().strip()
        self.assertEqual("Both players have blackjack! Draw!", output)

    def test_blackjack_results2(self):
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.dealer_hand = Hand(dealer=True)
        game.dealer_hand.add_card(Card("Spades", "A"))
        game.dealer_hand.add_card(Card("Clubs", "A"))
        game.player_hand = Hand(dealer=False)
        game.player_hand.add_card(Card("Diamonds", "A"))
        game.player_hand.add_card(Card("Hearts", "J"))
        player, dealer = game.check_for_blackjack()
        game.show_blackjack_results(player, dealer)
        output = out.getvalue().strip()
        self.assertEqual("You have blackjack! You win!", output)

    def test_blackjack_results3(self):
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.dealer_hand = Hand(dealer=True)
        game.dealer_hand.add_card(Card("Spades", "A"))
        game.dealer_hand.add_card(Card("Diamonds", "K"))
        game.player_hand = Hand(dealer=False)
        game.player_hand.add_card(Card("Clubs", "2"))
        game.player_hand.add_card(Card("Hearts", "5"))
        player, dealer = game.check_for_blackjack()
        game.show_blackjack_results(player, dealer)
        output = out.getvalue().strip()
        self.assertEqual("Dealer has blackjack! Dealer wins!", output)

