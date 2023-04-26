from blackjack import BlackJack


def main():
    keep_playing = True
    while keep_playing:
        game = BlackJack()
        result = game.play()
        print(f"{result}\n")
        answer = input(
            "Do you want to continue? Type 'n' to exit the game: ").lower().strip()
        if answer == 'n':
            keep_playing = False
        print()


if __name__ == "__main__":
    main()
