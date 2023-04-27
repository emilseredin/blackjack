from player import Player
from dealer import Dealer


class BlackJack:

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()

    def determine_winner(self) -> str:
        """
            Determine the winner according to the blackjack rules
            Player wins if one of the following is true:
                - Player has a score of 21
                - Dealer has a score greater than 21
                - Player's score is greater than dealer's score
        """
        dealer_too_many = self.dealer.score > 21
        player_over_dealer = self.player.score > self.dealer.score
        tie = self.player.score == self.dealer.score
        if tie:
            message = "It's a tie."
        elif dealer_too_many:
            message = "Too many for the dealer. You win!"
        elif player_over_dealer:
            message = "You win!"
        else:
            message = "You lose."
        return message


    def play(self) -> str:
        """
            Play one blackjack game
            Return result of the game
        """
        self.player.receive_cards(self.dealer.deal(cards=2))
        self.dealer.receive_cards(self.dealer.deal(cards=2)) 
        self.player.calculate_score()
        self.dealer.calculate_score()
        print(f"Your cards: {self.player.get_cards()}")
        print("Dealer's first card: {}".format(
            self.dealer.get_first_card()))
        # if the player has a blackjack, go straight to determining the winner
        if self.player.score == 21:
            print(f"Dealer's cards: {self.dealer.get_cards()}")
            return self.determine_winner()

        # if the player doesn't have a blackjack, proceed with the game
        # first, cards are dealt to the player 
        keep_dealing = True
        while keep_dealing:
            answer = input(
                "Type 'y' to get another card, type 'n' to pass: ").strip()
            if answer == 'n':
                keep_dealing = False
            else:
                new_card = self.dealer.deal()
                self.player.receive_cards(new_card)
                self.player.calculate_score()
                if self.player.score > 21:
                    keep_dealing = False
                print(f"\nYour cards: {self.player.get_cards()}")
        print(f"\nYour final score: {self.player.score}\n")
        print(f"Dealer's cards: {self.dealer.get_cards()}\n")
        if self.player.score > 21:
            return "Too many. You lose."

        # check if a dealer has blackjack
        if self.dealer.score == 21:
            return "Dealer has a Black Jack. You lose."
        # if not,  cards are dealt to the dealer
        keep_dealing = True
        while keep_dealing:
            # dealer must draw to 16
            if self.dealer.score > 16:
                keep_dealing = False
            else:
                new_card = self.dealer.deal()
                self.dealer.receive_cards(new_card)
                self.dealer.calculate_score()
                print(f"Dealer's cards: {self.dealer.get_cards()}")
        print(f"\nDealer's final score: {self.dealer.score}\n")
        return self.determine_winner()