# Using a While loop, count how many numbers are divisible by 4 between 1 and 100.


number = 1
while number <= 100:
    if number % 4 == 0:
        print(number)
    number = number + 1