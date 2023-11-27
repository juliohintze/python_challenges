# Keep asking for numbers from the user. Each time the user gives a number, print the number.
# If the user gives a non-numeric value, get out of the loop and let the script reach the end.

while True:
    userinp = input("do NOT give me a number... or else...\n")
    if not userinp.isnumeric():
        break
    else:
        print("ermmm ermmmm that iS A NUMBER!!!! A NUMBER!!!!\n")