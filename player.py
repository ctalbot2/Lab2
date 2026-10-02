"""
player.py
Cole Talbot
this program contains the Player class
10/2/2026
"""
from coin import Coin

class Player:
    def __init__(self, name, sideup):
        self.name = name
        self.wallet = 20
        self.coin = Coin(sideup)
    def toss_coin(self):
        self.coin.toss()
    def get_coin_side(self):
        return self.coin.get_sideup()
    def win_coin(self):
        self.wallet += 1
    def lose_coin(self):
        self.wallet -= 1
