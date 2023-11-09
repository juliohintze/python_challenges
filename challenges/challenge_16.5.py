# Ask for an input from the user. If the input is numeric, double it and print it. If not, print "Not number".

response = input("say something\n")
if response.isnumeric():
    print(int(response) * 2)
else:
    print("Not a NUMBER!!!!!!!!!!!!!")
