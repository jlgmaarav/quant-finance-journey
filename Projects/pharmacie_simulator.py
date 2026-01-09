import math
import random

class Pharmacie():
    def __init__(self, pharmacie_id, position, strategy, initial_stock):
        self.pharmacie_id = pharmacie_id
        self.position = position
        self.strategy = strategy
        self.stock = {"unusual": initial_stock}

        self.money = 0

    def try_sell(self):
        if self.stock["unusual"] > 0:
            self.stock["unusual"] -= 1

            self.money += 10

            return True
        else:
            return False
