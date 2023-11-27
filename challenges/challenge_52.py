# Create a Pet class.
# A Pet can have a name, can be hungry and can eat.
# A Pet always starts hungry.
# When a Pet eats, print that it's eating (use its name in the print message).
# After a Pet eats, it shouldn't be hungry anymore.
# Then create an object from that class, give it a name and make it eat.

class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger
    def feed(self):
        print("You feed", self.name)
        self.hunger = False


mango = Pet("Mango", True)
print(mango.hunger)
mango.feed()
print(mango.hunger)

sunny = Pet("Sunny", True)
print(sunny.hunger)
sunny.feed()
print(sunny.hunger)