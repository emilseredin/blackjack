from player import Player
from card import Card
from random import shuffle


class Dealer(Player):

    def __init__(self) -> None:
        self.shoe = [
            Card('2'),
            Card('3'),
            Card('4'),
            Card('5'),
            Card('6'),
            Card('7'),
            Card('8'),
            Card('9'),
            Card('10'),
            Card('J'),
            Card('Q'),
            Card('K'),
            Card('A')
        ] * 5
        shuffle(self.shoe)
        super().__init__()

    def deal(self, cards=1) -> list:
        drawn_cards = self.shoe[:cards]
        self.shoe = self.shoe[cards:]
        
        return drawn_cards
    
    def get_first_card(self) -> str:
        return self.cards[0].face