"""
coin.py
Cole Talbot
This class is one tossable coin
10/1/26
"""
import random

class Coin:
    def __init__(self, sideup):
        self.sideup = sideup

    def toss(self):
        result = random.randint(0,1)
        if result == 0:
            self.sideup = "Tails"
        else:
            self.sideup = "Heads"

    def get_sideup(self):
        return self.sideup