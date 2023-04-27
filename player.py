class Player:

    def __init__(self):
        self.cards = []
        self.score = 0

    def calculate_score(self) -> int:
        cards = sorted(self.cards, key=lambda card: card.value)
        score = 0
        for card in cards:
            if card.value == 11 and score + card.value > 21:
                score = score + 1
            else:
                score = score + card.value
        self.score = score

    def get_cards(self) -> list:
        return [card.face for card in self.cards]

    def get_first_card(self) -> str:
        return self.cards[0].face

    def receive_cards(self, cards) -> None:
        self.cards.extend(cards)
