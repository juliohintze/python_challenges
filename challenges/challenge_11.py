# Ask for two texts from the user and print the longest one.

text = input('tell me a joke\n')
text2 = input('that one sucked, tell me another\n')
if len(text) > len(text2):
    print(text)
else:
    print(text2)