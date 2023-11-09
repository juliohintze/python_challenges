# Insist for a number from 1 to 10 from the user, then print that number's multiplication table.

while True:
    p = input("gimme a number 1-10... IF YOU DARE\n")
    if p.isnumeric():
        for i in range(1, 13):
            print(i,'x',int(p),'=',i * int(p))

    else:
        print("I asked for a NUMBER!!!!! all I got was my day being ruined...") 