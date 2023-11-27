# Create a function that receives a number and returns True when it's even, or False when it's odd.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(5))

# number = number % 2 == 0