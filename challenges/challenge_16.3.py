# Keep asking for an input from the user. Every time he does, print the number of characters of the input.
# If the user types "EXIT", break the loop and print the number of times you received an input.

count = 0
while True:
    response = input("YOU'LL NEVER CATCH ME you you you y\nsay exit to leave :)\n")
    if response == "EXIT":
        print("bye byeeee!!")
        break
    else:
        count = count + 1
        print(len(response))
print(count)