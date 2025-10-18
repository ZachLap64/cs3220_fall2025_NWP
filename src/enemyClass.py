from src.thingClass import Thing
import random

class Enemy(Thing):

    def __init__(self, location=None):
        self.alive = True
        self.power = random.randint(10,40)*0.01*(49*0.75)
        self.location = location