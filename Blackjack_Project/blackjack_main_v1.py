# Blackjack with: Hong Rot, and 3 other classmates.
import random

general_deck = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'] * 4
current_game = 0


class BlackjackGame:
    def __init__(self):  # Holds the cards in the object
        self.current_deck = []
        self.player_hand = []
        self.dealer_hand = []

    def read_cards(self, person, dealer_show=False):  # Read cards for 'person'
        if person == "player":
            full_str = ""
            for data in self.player_hand:
                full_str += f"{data} "
            return full_str
        elif person == "dealer":  # Read dealers card, but hide the first card.
            full_str = ""
            cut_list = self.dealer_hand.copy()
            if not dealer_show:
                cut_list.pop(0)
            for data in cut_list:
                full_str += f"{data} "
            return full_str

    def read_total(self, person):  # Read total cards
        if person == "player":
            p_total = 0
            for card in self.player_hand:
                if card == "Jack" or card == "Queen" or card == "King":
                    p_total += 10
                elif not card == "Ace":  # Ace is not accounted for
                    p_total += int(card)
            for card in self.player_hand:
                if card == "Ace":  # Ace is now accounted for
                    if p_total + 11 > 21:  # If hand values over 21 with ace 11, turn an ace into 1
                        p_total += 1
                    else:
                        p_total += 11
            return p_total
        elif person == "dealer":  # Same as first if check, but for the dealer.
            d_total = 0
            for card in self.dealer_hand:
                if card == "Jack" or card == "Queen" or card == "King":
                    d_total += 10
                elif not card == "Ace":
                    d_total += int(card)
            for card in self.dealer_hand:
                if card == "Ace":
                    if d_total + 11 > 21:
                        d_total += 1
                    else:
                        d_total += 11
            return d_total

    def win_con(self):  # Standard win conditions
        if self.read_total("player") == 21 and self.read_total("dealer") != 21:  # Blackjack win
            print("\nYou Won with 21!\n")
            return "player_won"
        elif self.read_total("player") == 21 and self.read_total("dealer") == 21:  # Draw
            print("\nDraw with both having 21\n")
            return "draw"
        elif self.read_total("player") > 21:  # Player Bust
            print("\nLose, you've busted!\n")
            return "player_lost"
        elif self.read_total("dealer") == 21:  # Dealer Blackjack
            print("\nLose, dealer won with 21!\n")
            return "player_lost"
        elif self.read_total("dealer") > 21:  # Dealer Bust
            print("\nYou win, dealer busted!\n")
            print(f"You have {self.read_total('player')} over {self.read_total('dealer')}")
            return "player_won"
        else:
            return None

    def stand_win_con(self):  # Final win check condition.
        if self.read_total("player") > self.read_total("dealer"):  # Player win
            print(f"You won with {self.read_total('player')} over {self.read_total('dealer')}")
            return "player_won"
        elif self.read_total("player") < self.read_total("dealer"):  # Player bust check.
            if self.read_total("dealer") > 21:  # Dealer lost
                print(f"Dealer busted, you won with {self.read_total('player')} over {self.read_total('dealer')}")
                return "player_won"
            else:  # Dealer won
                print(f"You lost with {self.read_total('player')} under {self.read_total('dealer')}")
                return "player_lost"
        else:
            print("\nDraw\n")
            return "draw"

    def shuffle_deck(self):  # Refill, shuffle, and pass cards out.
        self.current_deck = general_deck.copy()
        for i in range(2):  # Only shuffle 2 cards per person.
            random.shuffle(self.current_deck)
            card = self.current_deck.pop()
            self.player_hand.append(card)
        for i in range(2):  # Dealer ver
            card = self.current_deck.pop()
            self.dealer_hand.append(card)

    def add_card(self, person):  # Add card to person, different but similar to shuffle.
        if person == "player":
            card = self.current_deck.pop()
            self.player_hand.append(card)
            return card
        elif person == "dealer":
            card = self.current_deck.pop()
            self.dealer_hand.append(card)
            return card

    def dealer_turn(self):  # Dealer A.I.
        if self.read_total("dealer") < 17:  # If less than 17, draw a card
            newest_card = self.add_card("dealer")
            print(f"Dealer got a {newest_card}")
            return self.win_con()  # Check if new card makes it over 21
        else:  # If dealer does not hit, end game.
            print("Dealer is not hitting.")
            print("\nChecking scores.\n")
            return self.stand_win_con()


play_input = input("""−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Would you like to play blackjack? (y/n)
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n>""").lower()
if play_input == "yes" or play_input == "y":
    print("""   Rules
This version is a turned based game.
Aces are 11 unless if hand is above 21, which then turns to 1.
Dealer will hit until it's hand is at least 17
in which the the game will end if you stand or bust.
    """)
    input("Press enter to continue.")
    active = True
    while active:  # Loop to keep you playing
        current_game += 1
        print(f"\nCurrent game: {current_game}\n")
        game = BlackjackGame()
        game.shuffle_deck()
        while True:
            check_win = game.win_con()  # Always checks win condition at start
            if check_win:
                print(f"Dealer had the cards: {game.dealer_hand}")
                print(f"You had the cards: {game.player_hand}")
                try_again = input("\nPlay again? (y/n)").lower()
                while try_again != "n" and try_again != "y" and try_again != "no" and try_again != "yes":
                    try_again = input("\nPlay again? (y/n)").lower()
                if try_again == "n" or try_again == "no":
                    active = False
                break
            print("Dealer currently showing: \n", game.read_cards("dealer"))
            print("You have: \n", game.read_cards("player"))
            print("\nYou have total of", game.read_total('player'))
            hand_input = input("[H]it or [S]tand or [Q]uit?\n>").lower()
            while hand_input != "h" and hand_input != "s" and hand_input != "q":
                hand_input = input("[H]it or [S]tand or [Q]uit?\n>").lower()
            if hand_input == "h":  # Hit
                new_card = game.add_card("player")
                print(f"Hitting; You got {new_card}")
                if game.read_total("player") > 21:  # win condition here, don't mind it.
                    print("You busted!\n")
                    print(f"Dealer had the cards: {game.read_cards('dealer', True)}")
                    print(f"You had the cards: {game.read_cards('player')}")
                    try_again = input("\nPlay again? (y/n)").lower()
                    while try_again != "n" and try_again != "y" and try_again != "no" and try_again != "yes":
                        try_again = input("\nPlay again? (y/n)").lower()
                    if try_again == "n" or try_again == "no":
                        active = False
                    break
                checker = game.dealer_turn()  # Debug line below.
                # print("WIN_CON_CHECK 1", checker, "DEALER TOTAL: ", game.dealer_hand, game.read_total("dealer"))
                if checker == "player_lost" or checker == "player_won" or checker == "draw":
                    print(f"Dealer had the cards: {game.read_cards('dealer', True)}")
                    print(f"You had the cards: {game.read_cards('player')}")
                    try_again = input("\nPlay again? (y/n)").lower()
                    while try_again != "n" and try_again != "y" and try_again != "no" and try_again != "yes":
                        try_again = input("\nPlay again? (y/n)").lower()
                    if try_again == "n" or try_again == "no":
                        active = False
                    break
            elif hand_input == "s":  # Stand
                print("You decided to stand.")
                checker = game.dealer_turn()  # Debug line below.
                # print("WIN_CON_CHECK 2", checker, "DEALER TOTAL: ", game.dealer_hand, game.read_total("dealer"))
                if checker == "player_lost" or checker == "player_won" or checker == "draw":
                    print(f"Dealer had the cards: {game.read_cards('dealer', True)}")
                    print(f"You had the cards: {game.read_cards('player')}")
                    try_again = input("\nPlay again? (y/n)").lower()
                    while try_again != "n" and try_again != "y" and try_again != "no" and try_again != "yes":
                        try_again = input("\nPlay again? (y/n)").lower()
                    if try_again == "n" or try_again == "no":
                        active = False
                    break
            elif hand_input == "q":
                active = False
                break
    print("Goodbye then.")
else:
    print("GOODBYE!")
