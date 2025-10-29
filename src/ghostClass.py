from src.thingClass import Thing
import random

class Ghost(Thing):

    def __init__(self, location=None):
        self.alive = True
        self.location = location