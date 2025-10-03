from Food import Food
import random

class Sausage(Food):
    def __init__(self):
        self.calories = 6
        self.weight = random.randint(1,20)
