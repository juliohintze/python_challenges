# Keep asking for an input from the user. Every time he does, print the number of characters of the input.
# If the user types "EXIT", break the loop.


while True:
    response = input("give up\n")
    if response == "EXIT":
        print("fine. have it your way")
        break
    else:
        print(len(response))