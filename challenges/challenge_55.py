# Create the same Pet and Cat classes from the challenge 47,
# and then create a Dog class as a child of Pet.
# A Dog is a Pet that can bark. When it barks, print its name (like "Mel: WOOF!")
# Create an object from the Pet class and make it eat and meow.
# Create an object from the Dog class and make it eat and bark.

class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger
    def feed(self):
        print("You feed", self.name)
        self.hunger = False
    def hunger_status(self):
        print(self.name, "hunger", "=", self.hunger)
class Dog(Pet):
    def bark(self):
        print(self.name, "says hi and barks!")
    def jump(self):
        print(self.name, "looks at you and jumps up and down")

mel_gibson = Dog("Mel Gibson", True)
mel_gibson.hunger_status()
mel_gibson.bark()
mel_gibson.feed()
mel_gibson.hunger_status()
mel_gibson.jump()