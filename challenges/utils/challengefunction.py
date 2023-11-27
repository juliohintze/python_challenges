def forcenumber():
    userinput = input("GIMME A NUMBER\n")
    while True:
        if not userinput.isnumeric():
            print("THAT'S NOT A NUMBER!!!!!")
        else:
            print(userinput)