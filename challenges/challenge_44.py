# Guessing game! Choose a number from 1 to 100. Then, in a while loop, ask the user to guess the number.
# When the user fails, give him a hint (if the given number is greater or less than the secret number).
# When the user wins, end the program.

correct_number = 27

while True:
    numberuser = input("I BET YOU WON'T GUESS MY NUMBER!!! I'M SMART AND YOU'RE DUMB\n")
    if int(numberuser) > correct_number:
        print("you're getting COLD!!! it's lower.")
        if int(numberuser) == 69:
            print("hehehehe")
    elif int(numberuser) < correct_number:
        print("NOPE!!! WAHAHAHHHAHHAHHAHAA it's higher... dummy.")
    else:
        print("oh... nooooo.... :(")
        break