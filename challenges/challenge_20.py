# Keep asking for text from the user. Each time the user gives a text, print the number of characters that text has.
# If the text is "EXIT", get out of the loop and let the script reach the end.

while True:
    userinp = input("gimme text!!\n")
    if userinp == "EXIT":
        break
    else:
        print(len(userinp))

# while True:
#     userinp = input("gimme text!!\n")
#     if print(len(userinp)):
#         if userinp == "EXIT":
#             break