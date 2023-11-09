# Get a number from the user and then, using a While loop, print the multiplication table of that number.

text = input("gimme a number!!\n")
number = 1

while number <= 12:
    print(int(text) * number)
    number = number + 1