# Ask for an input from the user. Print "Number" if the input is numeric, if not print "Not number".

inp = input("gimme text or a number, your choice!!\n")

if inp.isnumeric():
    print("Number")
else:
    print("Not number")