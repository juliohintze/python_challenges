# Insist for a number greater than 10. When you get it, print the even numbers between 1 and the given number.

while True:
    numb = input("gimme a number greater than 10... I'll tell you a funny joke!!\n")
    if numb.isnumeric() and int(numb) > 10 and int(numb) % 2 == 0:
        break
    else:
        print("try that again")
print("good job IDIOT")
even = 0
while even <= int(numb):
    print(even)
    even = even + 2
print("YOU'RE the joke")

