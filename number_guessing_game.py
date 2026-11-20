import random as rd

computer = rd.randint(1, 100)

while True:
    try:
        player = int(input("Guess the number I'm thinking of: "))
        if player > computer:
            print("Too high")
        elif player < computer:
            print("Too low")
        else:
            print("Correct 👊👏")
            break
    except ValueError:
        print("Wrong input")
