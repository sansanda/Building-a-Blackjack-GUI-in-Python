from Logic.Deck import Deck
from Logic.Hand import Hand

class Game:

    def __init__(self):
        pass

    def play(self):
        playing = True

        while playing:

            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Your hand is: ")
            self.player_hand.display()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            game_over = False

            while not game_over:

                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue #Este continue nos sacará fuera del while

                choice = input("Please choose [Hit/Stick] ").lower()
                while choice not in ["h","s","hit","stick"]:
                    choice = input("H, S, h, s, Hit or Stick").lower()

                if choice in ["h", "hit"]:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()

                    if self.player_is_over():
                        print("You have lost!")
                        game_over = True

                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print("Final Results!")
                    print("Your hand's value is: ", player_hand_value)
                    print("Dealer's hand value is: ", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You win!!!")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!!!")
                    else:
                        print("Dealer wins!!!")

                    game_over = True

            again = input("Play again? [Y/N] ").lower()
            while again not in ["y","n"]:
                again = input("Please enter Y or N ").lower()
            if again == "n":
                print ("Thanks for playing!!!")
                playing = False
            else:
                game_over = False # Es necesario??

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):

        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")
        elif player_has_blackjack:
            print("You have blackjack! You win!")
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")

    def player_is_over(self):
        return self.player_hand.get_value() > 21

if __name__ == "__main__":
    game = Game()
    game.play()