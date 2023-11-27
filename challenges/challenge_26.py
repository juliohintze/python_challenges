# Ask for a text from the user. Print the text without its first 10 characters.

user = input("Please leave me alone, don't talk to me.\n")
start = len(user) - 10
end = len(user)
trimmedtext = user[start:end]

print(trimmedtext)
print("Yeah that's what you get for bothering me")