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
            print(f"{player1.get_name()} has {player1.get_wallet()} coins")
            print(f"{player2.get_name()} has {player2.get_wallet()} coins")
        elif choice == "n":
            print("--- Final Score ---")
        else:
            print("I didn't understand your choice. Please enter either y or n")


main()