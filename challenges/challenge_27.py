# Ask for a number (n) and text from the user. Print the first (n) characters from the given text.

user = input("now say something!!\n")
usertxt = int(input("gimme a number\n"))
trimmedtxt = user[0:usertxt]

print(trimmedtxt)