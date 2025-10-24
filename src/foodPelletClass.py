from src.thingClass import Thing
import random

class FoodPellet(Thing):

    def __init__(self, location=None):
        self.location = location