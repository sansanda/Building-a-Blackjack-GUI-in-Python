from Logic.Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = [Card(s,v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
                                for v in [  "A","2","3","4","5","6","7","8","9","10",
                                            "J","Q","K"]
                    ]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1: #No acabo de entender porque no es len(self.cards) > 0
            return self.cards.pop(0)
