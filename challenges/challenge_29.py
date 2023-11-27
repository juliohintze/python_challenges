# Create a function that insists for a number from the user. Use it to get a number from the user and print the result.
# Create that function in a separate file in the "utils" folder and import the function when you need to use it.
# Then after that, refactor the challenges 17, 18 and 19 to use this function instead.

# Insist for two numbers, add them together and print the result


# can't seem to use isnumeric, I need another way to check...?
# defining a variable above my DIY function seems to make it void, and putting it IN the loop doesn't work. I can't seem to do that.
# ok nvm I made it work LMAO, it was the order. I need to define in above the "body" (that's what everything says that's called?)

def forcenumber():
    userinput = input("GIMME A NUMBER\n")
    if not userinput.isnumeric():
        print("THAT'S NOT A NUMBER!!!!!")
    else:
        return int(userinput)


num1 = forcenumber()
num2 = forcenumber()

print(num1 + num2)