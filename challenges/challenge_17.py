# Ask for a number from 1 to 10 from the user. While the user doesn't give a number from 1 to 10, keep asking. When he does, print it.
# For future challenges, this will be called "Insist".


while True:
    number = input("I bet you won't give me a number between 1 and 10...\n")
    
    if number.isnumeric():
        if int(number) in range(1, 11):
            print(int(number))
        else:
            print("you lied to me.")
    else:
        print("THAT'S NOT A NUMBER!!!!!!!!!!!!!!!!!!!")