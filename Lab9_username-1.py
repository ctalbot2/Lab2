"""
Lab9_username-1.py
Cole Talbot
The purpose of the program,
Any info about starter code (If used, where it came from, link, etc.), and the
10/2/2026
"""
from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    
    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins")

    while True:
        choice = input("Do you want to toss the coins? y/n: ")
        if choice == "y":
            print("\n Tossing...")
            player1.toss_coin()
            player2.toss_coin()

            if player1.get_coin_side() == player2.get_coin_side():
                player1.win_coin()
                player2.lose_coin()
                print("It's a match.  Player 1 wins a coin")

            else:
                player2.win_coin()
                player1.lose_coin()
                print("No match! Player 2 wins a coin")


            print(f"{player1.get_name()} tossed {player1.get_coin_side()}")
            print(f"{player2.get_name()} tossed {player2.get_coin_side()}")
            

            print(f"{player1.get_name()} has {player1.get_wallet()} coins")
            print(f"{player2.get_name()} has {player2.get_wallet()} coins")

        elif choice == "n":
            break

        else:
            print("I didn't understand your choice. Please enter either y or n")

    print("--- Final Score ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 finished with more coins.  Player 1 wins!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 finished with more coins.  Player 2 wins!")
    else:
        print("It's a draw!")

main()