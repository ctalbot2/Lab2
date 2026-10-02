"""
The program's name,
Your name (the author),
The purpose of the program,
Any info about starter code (If used, where it came from, link, etc.), and the
Date.
"""
from coin import Coin

class Player:
    def __init__(self, name, sideup):
        self.name = name
        self.wallet = 20
        self.coin = Coin(sideup)