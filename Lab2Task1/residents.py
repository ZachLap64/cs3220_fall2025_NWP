from src.thingClass import Thing

class Milk(Thing):
    def __init__(self):
        self.status = 'milk'


class Mouse(Thing):
    def __init__(self):
        self.status = 'mouse'


class Dog(Thing):
    def __init__(self):
        self.status = 'dog'