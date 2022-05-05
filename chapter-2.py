first_name = "arnab"
last_name="saha"
full_name= first_name+""+last_name
print(full_name)      #No Error
print(full_name+3)  # error  //becuse types are different here
print(full_name+"3")      #No Error      
print(full_name+str(3))      #No Error   //make 3 a str
print(full_name*3)      #No Error       //multiplies name for 3 times


name=input("your name is : ")
print("your name is : " + name)   #we get inputs always in strings

number_1 = input("type your first number : ")
number_2 = input("type your second number : ")
sum_of_numbers= int(number_1)+int(number_2)
print("total number is : "+str(sum_of_numbers))
print(float(4))

name,age="arnab",20
print("hey, "+name+" your age is : "+str(age)+" right")
x=y=z=1
print(x+y+z)

name,age=input("enter your name and age (space separated) : ").split()
print("hey, "+name+" your age is : "+str(age)+" right")

name,age=input("enter your name and age (comma separated) : ").split(",")
print("hey, "+name+" your age is : "+str(age)+" right")
#string formating 
#for python 3.6
print(f"hello {name} your age is {age}")

a,b,c=input("type any three numbers (comma separated): ").split(",")
print(f"avarage of these 3 numbers is : {(int(a)+int(b)+int(c))/3}")

lan = "python"
print(lan[0]) #we start with 0 it we go left to right
print(lan[-1]) #we start with -1 it we go right to left

# [start argument : stop argument-1]
print(lan[:])  #if we pass no argument then it will show whole string
print(lan[1:]) #if we pass only starting argument it start from the staring argument and go to end of the string
print(lan[:-3]) #if we pass only ending argument it start from beginning and end to before the ending argument.
print(lan[2:5]) #if we pass both argument it start from starting argument and to before the ending argument.

# [start argument : stop argument-1 : step]
print("arnabsaha"[2:9:1]) # step=1, no changes
print("arnabsaha"[2:9:2]) # step=2, 1 step later
print("arnabsaha"[2:9:-1]) # step=-1, reverse order
print("arnabsaha"[::-1]) # step=-1, reverse order 

# name=input("type your full name : ")
# print(f"your name in reverse is : {name[::-1]}")

name="           ......aRnaB saHa......          "
print(len(name)) #length function counts spaces also
print(name.lower()) #make it in lowercase
print(name.upper()) #make it in uppercase
print(name.title()) #make it as like title
print(name.count("a")) #counts how much times that letter is in that string
print(name.lstrip()) #remove left spaces
print(name.rstrip()) #remove right spaces
print(name.strip()) #remove left right both spaces


name,char=input("type your name and a letter (comma separated): ").split(",")
print(len(name.strip()))
print(name.lower().strip().count(char.strip()))

string="she is so beautiful, she is a good dancer too"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1)) # 1 signifies when it will replace only one is

print(string.find("is")) #it will give index of first is
print(string.find("is",8)) #it will give index of first is after index 8
print(string.find("is",string.find("is")+1)) #it will give index of second is

name="arnab"
print(name.center(7,":"))
print(name.center(len(name)+8,"*"))