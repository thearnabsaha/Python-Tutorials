first_name = "arnab"
last_name="saha"
full_name= first_name+""+last_name
print(full_name)      #No Error
# print(full_name+3)  // error  //becuse types are different here
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