from Food import Food
import random

class Milk(Food):
    def __init__(self):
        self.calories = 3
        self.weight = random.randint(1,10)