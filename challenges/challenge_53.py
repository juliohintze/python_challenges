# Create the same Pet class as the challenge 45,
# but this time use the __init__ function to get the
# name of the pet in the class initialization.
# Then create an object from that class and make it eat.

class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger
    def feed(self):
        print("you feed", self.name)
        self.hunger = False

mango = Pet("Mango", True)
print(mango.hunger)
mango.feed()
print(mango.hunger)