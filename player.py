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
