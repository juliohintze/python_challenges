# This code is supposed to insist for a number,
# but it seems to accepts non-numeric values too.

# user_response = input("Give me a number: ")
# while True:
#   if not user_response.isnumeric:
#     print("THAT'S NOT A NUMBER!!")
#   else:
#     print("Very good!")
#     break

while True:
    user_response = input("Give me a number: ")
    if not user_response.isnumeric():
        print("THAT'S NOT A NUMBER!!")
    else:
        print("Very good!")
        break