# FizzBuzz challenge
# Print the numbers from 1 to 100 (including 100), but:
# - If the number is divisible by 3, instead of printing the number, print the word "Fizz"
# - If the number is divisible by 5, instead of printing the number, print the word "Buzz"
# - If the number is divisible by both 3 AND 5, instead of printing the number, print the word "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i,": " "FizzBuzz")
    elif i % 3 == 0:
        print(i,": " "Fizz")
    elif i % 5 == 0:
        print(i,": " "Buzz")
    else:
        print(i)
        

