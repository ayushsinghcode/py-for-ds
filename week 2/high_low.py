import random
choice= random.randint(1,100)
while True:
    user_input=int(input("enter the number"))
    print(choice)
    if user_input != choice:
        if user_input>choice:
            print("lower")
        else:
            print("higher")
    else:
        print("you won")