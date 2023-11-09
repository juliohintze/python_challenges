# Insist for two numbers from the user. Then print the product of those numbers (one times the other).

while True:
    num1 = input("gimme a number\n")
    num2 = input("gimme ANOTHER number\n")
    if num1.isnumeric() and num2.isnumeric():
        print(num1, "x", num2,"=", int(num1) * int(num2))
    else:
        print("I SAID GIVE ME A NUMBER")

# 5 x 2 = 10