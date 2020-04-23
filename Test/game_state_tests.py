import unittest
import tkinter as tk

from Logic.GameState import GameState
from Logic.Hand import Hand
from Logic.Card import Card

class UnitTests(unittest.TestCase):

    def test_someone_has_blackjack_3(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "J"))
        gameState.player_hand.add_card(Card("Hearts", "A"))

        gameState.dealer_hand.add_card(Card("Spades", "A"))
        gameState.dealer_hand.add_card(Card("Clubs", "Q"))

        self.assertEqual(gameState.someone_has_blackjack(), "dp",
                         "Expected both the dealer and the player to have blackjack")

    def test_someone_has_blackjack_2(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "2"))
        gameState.player_hand.add_card(Card("Hearts", "2"))

        gameState.dealer_hand.add_card(Card("Spades", "A"))
        gameState.dealer_hand.add_card(Card("Clubs", "Q"))

        self.assertEqual(gameState.someone_has_blackjack(), "d", "Expected the dealer to have blackjack")

    def test_someone_has_blackjack_1(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "A"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "2"))
        gameState.dealer_hand.add_card(Card("Clubs", "2"))

        self.assertEqual(gameState.someone_has_blackjack(), "p", "Expected the player to have blackjack")

    def test_hit_method_4(self):

        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "J"))
        gameState.player_hand.add_card(Card("Hearts", "8"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "A"))
        gameState.dealer_hand.add_card(Card("Clubs", "J"))

        winner = gameState.hit()

        self.assertEqual(winner, 'd', "Expected the dealer to have blackjack")

    def test_hit_method_1(self):

        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "J"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "2"))
        gameState.dealer_hand.add_card(Card("Clubs", "2"))

        winner = gameState.hit()

        self.assertTrue(gameState.player_hand.get_value() > 20,
                        "Expected the value of the player's hand to be greater than 20")
        self.assertEqual(gameState.dealer_hand.get_value(), 4,
                         "Expected the value of the dealer's hand to be equal to 4")
        self.assertTrue(winner == 'd', "Expected the dealer to win")

    def test_get_table_state_5(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "A"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "A"))
        gameState.dealer_hand.add_card(Card("Clubs", "K"))

        table_state = gameState.get_table_state()
        print(table_state)

        expected_state = {
            'player_cards': [Card("Diamonds", "A"), Card("Hearts", "J")],
            'dealer_cards': [Card("Spades", "A"), Card("Clubs", "K")],
            'has_winner': 'dp',
            'blackjack': True,
        }

        self.assertEqual(str(expected_state['player_cards']), str(table_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_state['dealer_cards']), str(table_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('dp', table_state['has_winner'], "The results were expected to be a tie")
        self.assertEqual(True, table_state['blackjack'], "The winners were expected to have blackjack")

    def test_get_table_state_4(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "K"))
        gameState.player_hand.add_card(Card("Diamonds", "6"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "2"))
        gameState.dealer_hand.add_card(Card("Clubs", "2"))

        table_state = gameState.get_table_state()

        expected_state = {
            'player_cards': [Card("Diamonds", "K"), Card("Diamonds", "6"), Card("Hearts", "J")],
            'dealer_cards': [Card("Spades", "2"), Card("Clubs", "2")],
            'has_winner': False,
            'blackjack': False,
        }

        self.assertEqual(str(expected_state['player_cards']), str(table_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_state['dealer_cards']), str(table_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual(False, table_state['has_winner'], "The player was not expected to win")
        self.assertEqual(False, table_state['blackjack'], "The winner was not expected to have blackjack")

    def test_get_table_state_3(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "5"))
        gameState.player_hand.add_card(Card("Diamonds", "6"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "2"))
        gameState.dealer_hand.add_card(Card("Clubs", "2"))

        table_state = gameState.get_table_state()

        expected_state = {
            'player_cards': [Card("Diamonds", "5"), Card("Diamonds", "6"), Card("Hearts", "J")],
            'dealer_cards': [Card("Spades", "2"), Card("Clubs", "2")],
            'has_winner': 'p',
            'blackjack': True,
        }

        self.assertEqual(str(expected_state['player_cards']), str(table_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_state['dealer_cards']), str(table_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('p', str(table_state['has_winner']), "The player was expected to have won")
        self.assertEqual(True, table_state['blackjack'], "The winner was expected to have blackjack")

    def test_get_table_state_2(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "2"))
        gameState.player_hand.add_card(Card("Hearts", "2"))

        gameState.dealer_hand.add_card(Card("Spades", "A"))
        gameState.dealer_hand.add_card(Card("Clubs", "J"))

        table_state = gameState.get_table_state()

        expected_state = {
            'player_cards': [Card("Diamonds", "2"), Card("Hearts", "2")],
            'dealer_cards': [Card("Spades", "A"), Card("Clubs", "J")],
            'has_winner': 'd',
            'blackjack': True,
        }

        self.assertEqual(str(expected_state['player_cards']), str(table_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_state['dealer_cards']), str(table_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('d', str(table_state['has_winner']), "The dealer was expected to have won")
        self.assertEqual(True, table_state['blackjack'], "The winner was expected to have blackjack")

    def test_get_table_state_1(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "A"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "2"))
        gameState.dealer_hand.add_card(Card("Clubs", "2"))

        table_state = gameState.get_table_state()

        expected_state = {
            'player_cards': [Card("Diamonds", "A"), Card("Hearts", "J")],
            'dealer_cards': [Card("Spades", "2"), Card("Clubs", "2")],
            'has_winner': 'p',
            'blackjack': True,
        }

        self.assertEqual(str(expected_state['player_cards']), str(table_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_state['dealer_cards']), str(table_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('p', str(table_state['has_winner']), "The player was expected to have won")
        self.assertEqual(True, table_state['blackjack'], "The winner was expected to have blackjack")

    def test_get_final_state_4(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "2"))
        gameState.player_hand.add_card(Card("Hearts", "2"))
        gameState.player_hand.add_card(Card("Hearts", "7"))

        gameState.dealer_hand.add_card(Card("Spades", "A"))
        gameState.dealer_hand.add_card(Card("Clubs", "A"))

        final_state = gameState.calculate_final_state()
        expected_final_state = {
            'player_cards': [Card("Diamonds", "2"), Card("Hearts", "2"), Card("Hearts", "7")],
            'dealer_cards': [Card("Spades", "A"), Card("Clubs", "A")],
            'has_winner': 'd',
        }

        self.assertEqual(str(expected_final_state['player_cards']), str(final_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_final_state['dealer_cards']), str(final_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('d', final_state['has_winner'])

    def test_get_final_state_3(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "2"))
        gameState.player_hand.add_card(Card("Hearts", "2"))

        gameState.dealer_hand.add_card(Card("Spades", "A"))
        gameState.dealer_hand.add_card(Card("Clubs", "J"))

        final_state = gameState.calculate_final_state()
        expected_final_state = {
            'player_cards': [Card("Diamonds", "2"), Card("Hearts", "2")],
            'dealer_cards': [Card("Spades", "A"), Card("Clubs", "J")],
            'has_winner': 'd',
        }

        self.assertEqual(str(expected_final_state['player_cards']), str(final_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_final_state['dealer_cards']), str(final_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('d', final_state['has_winner'], "The dealer was expected to win")

    def test_get_final_state_2(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "6"))
        gameState.player_hand.add_card(Card("Hearts", "5"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "2"))
        gameState.dealer_hand.add_card(Card("Clubs", "2"))

        final_state = gameState.calculate_final_state()
        expected_final_state = {
            'player_cards': [Card("Diamonds", "6"), Card("Hearts", "5"), Card("Hearts", "J")],
            'dealer_cards': [Card("Spades", "2"), Card("Clubs", "2")],
            'has_winner': 'p',
        }

        self.assertEqual(str(expected_final_state['player_cards']), str(final_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_final_state['dealer_cards']), str(final_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('p', final_state['has_winner'], "The player was expected to win")

    def test_get_final_state_1(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()
        gameState.dealer_hand = Hand(dealer=True)

        gameState.player_hand.add_card(Card("Diamonds", "A"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        gameState.dealer_hand.add_card(Card("Spades", "2"))
        gameState.dealer_hand.add_card(Card("Clubs", "2"))

        final_state = gameState.calculate_final_state()
        expected_final_state = {
            'player_cards': [Card("Diamonds", "A"), Card("Hearts", "J")],
            'dealer_cards': [Card("Spades", "2"), Card("Clubs", "2")],
            'has_winner': 'p',
        }

        self.assertEqual(str(expected_final_state['player_cards']), str(final_state['player_cards']),
                         "The player's cards did not match the expected state")
        self.assertEqual(str(expected_final_state['dealer_cards']), str(final_state['dealer_cards']),
                         "The dealer's cards did not match the expected state")
        self.assertEqual('p', final_state['has_winner'], "The player was expected to win")

    def test_player_score_3(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()

        gameState.player_hand.add_card(Card("Diamonds", "A"))
        gameState.player_hand.add_card(Card("Hearts", "J"))

        expected_msg = "Score: 21"
        msg = gameState.player_score_as_text()

        self.assertEqual(expected_msg, msg, "Double check the output format of the string")

    def test_player_score_2(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()

        gameState.player_hand.add_card(Card("Diamonds", "8"))
        gameState.player_hand.add_card(Card("Hearts", "4"))
        gameState.player_hand.add_card(Card("Clubs", "5"))

        expected_msg = "Score: 17"
        msg = gameState.player_score_as_text()
        print(msg)

        self.assertEqual(expected_msg, msg, "Double check the output format of the string")

    def test_player_score_1(self):
        root = tk.Tk()

        gameState = GameState()
        gameState.player_hand = Hand()

        gameState.player_hand.add_card(Card("Diamonds", "2"))
        gameState.player_hand.add_card(Card("Hearts", "2"))

        expected_msg = "Score: 4"
        msg = gameState.player_score_as_text()
        print(msg)

        self.assertEqual(expected_msg, msg, "Double check the output format of the string")

