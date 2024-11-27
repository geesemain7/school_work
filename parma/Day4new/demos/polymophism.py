class Animal:
    def say(self):
        raise NotImplementedError("Abstract method")

class Dog(Animal):
    def __init__(self, name):
        self._name = name
    def say(self):
        print("I am", self._name, "Dog.",
              "I say: WOOF!")

class Cat(Animal):
    def __init__(self, name):
        self._name = name
    def say(self):
        print("I am", self._name, "Cat.",
              "I say: MEOW!")

class Pig(Animal):
    def __init__(self, name):
        self._name = name
    def say(self):
        print("I am", self._name, "Pig.")

def main():
    d = Dog("dogecoin bastard")
    c = Cat("small bastard")
    p1 = Pig("dirty bastard")
    p2 = Pig ("slightly less dirty bastard")

    animals = [d, c, p1, p2]

    for a in animals:
        a.say()

main()