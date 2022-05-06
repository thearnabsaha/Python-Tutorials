# import random
# winningNumber=random.randint(0,100)
# print(winningNumber)
# yourNumber=int(input("choose a number between 0-100: "))
# if winningNumber==yourNumber:
#     print("you win the game")
# else:
#     if winningNumber>yourNumber:
#         print("your number is too low")
#     if winningNumber<yourNumber:
#         print("your number is too low")
# # if winningNumber==yourNumber:
# #     print("you win the game")
# # elif winningNumber>yourNumber:
# #     print("your number is too low!!!")
# # elif winningNumber<yourNumber:
# #     print("your number is too high!!!")

# name,age= input("type your name and age (comma separated): ").split(",")
# if name=="abc" or age=="20":
#     print("good to go!!")
# else:
#     print("sorry no entry!!")

# name,age= input("type your name and age (comma separated): ").split(",")
# if name.strip().lower()[0]=="a" and int(age) >10:
#     print("you can watch coco!!")
# else:
#     print("sorry you can't watch coco!!")
# age=int(input("type your age: "))
# if age<=0:
#     print("your age is invalid")
# elif age<18:
#     print("your age is low!! so, you can't vote!!")
# elif age==18:
#     print("so, this is your first vote")
# else:
#     print("yes sir you can vote!!")
# name="arnab saha"
# if "a" in name:
#     print("yes present here!!!")
# else:
#     print("no! not present.")
# name=input("type your name: ")
# if name:
#     print(f"you name is {name}")
# else:
#     print("you didn't type anything!")
# i=1
# while i<=10:
#     print(f"hello world {i}")
#     i=i+1
# print("i'm arnab")
# i=0
# total=0
# while i<=10:
#     total+=i
#     i+=1
# print(total)
# i=0
# total=0
# tillSum=int(input("type any number: "))
# while i<=tillSum:
#     total+=i
#     i+=1
# print(total)
# number=(input("type some more than 1 letter number: "))
# i=0
# total=0
# while i<len(number):
#     total+=int(number[i])
#     i+=1
# print(total)
# name=input("type your name: ")
# i=0
# temp=""
# while i<int(len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]} : {name.count(name[i])}")
#         temp+=name[i]
#     i+=1
# while True:
#     print("chutiya")
# for i in range(10):
#     print(f"arnab is best {i}")
# for i in range(6,11):
#     print(f"arnab is best {i}")
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
import random
winnigNumber= random.randint(1,100)
willWin=True
i=1
while willWin:
    yourNumber=int(input("choose a number between 1-100: "))
    if winnigNumber==yourNumber:
        print(f"you win!!! you guessed it in {i} times")
        willWin=False
    elif winnigNumber<yourNumber:
        print("too high!!! guess again")
    elif winnigNumber>yourNumber:
        print("too low!! guess again")
    i+=1