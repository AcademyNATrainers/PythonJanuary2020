
class Dog:
    def __init__(self, name = 'Unnamed'):
        self.name = name

    def speak(self):
        print ("Woof")


class Cat:
    def __init__(self, name = 'Unnamed'):
        self.name = name

    def speak(self):
        print ("Meow")


class Conure:
    def __init__(self, name = 'Unnamed'):
        self.name = name

    def speak(self):
        print ("SQUAWK")


animals = [Dog("Spot"), Cat("Muffin"), Conure("Lio")]


def all_talk(pets):
    for pet in pets:
        pet.speak()


all_talk(animals)


