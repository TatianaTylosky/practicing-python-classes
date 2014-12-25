class Cat(object):
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        self.owner = None

class Owner(object):
    def __init__(self, name, dollars):
        self.name = name
        self.money = dollars
        self.cats = []

class Pet_store(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cats = []

