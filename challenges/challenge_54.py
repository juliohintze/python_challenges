# Create the same Pet class as the challenge 46,
# then create the child class Cat, that can meow.
# When a Cat meows, it prints the name of the cat AND the meow. Like "Mango: MEOW!"
# Then create an object from the Cat class. Make it eat and meow.

class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger
    def feed(self):
        print("You feed", self.name)
        self.hunger = False
class Cat(Pet):
    def meow(self):
        print(self.name, "meows VERY loud!!")

raptor = Cat("Raptor", True)
print("Hunger =", raptor.hunger)
raptor.meow()
raptor.feed()
print("Hunger =", raptor.hunger)