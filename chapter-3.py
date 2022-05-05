import random
winningNumber=random.randint(0,100)
yourNumber=int(input("choose a number between 0-100: "))
if winningNumber==yourNumber:
    print("you win the game")
elif winningNumber>yourNumber:
    print("your number is too low!!!")
elif winningNumber<yourNumber:
    print("your number is too high!!!")