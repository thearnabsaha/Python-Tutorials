# class Person:
#     def __init__(self,firstName,lastName,age):
#         #instance Variables
#         self.firstName=firstName
#         self.lastName=lastName
#         self.age=age

# p1=Person("arnab","saha",20)
# p2=Person("ambitama","saha",21)
# print(p1.age)
# print(p2.firstName+" "+p2.lastName)

# class Laptop:
#     def __init__(self,brand,name,price):
#         self.brand=brand
#         self.name=name
#         self.price=price
#     def applyDiscount(self,n):
#         print(self.price-(self.price*n/100))
#     @classmethod
#     def fromString(cls,string):
#         brand,name,price=string.split(",")
#         return (brand,name,price)
#     @staticmethod
#     def hello():
#         print("hi from static method")
# Laptop.hello()
# l3=Laptop.fromString("apple,mac,200000")
# print(l3)
# l1=Laptop("acer","nitro",40000)
# l2=Laptop("apple","macbook",130000)
# print(l1.brand)
# print(l2.name)
# l1.applyDiscount(40)

# class Person:
#     def __init__(self,firstNaeme,LastName):
#         self.firstName=firstNaeme
#         self.lastName=LastName
#     def fullName(self):
#         print(f"your full name is {self.firstName} {self.lastName}")
# p1=Person("arnab","saha")
# p2=Person("ambitama","saha")
# print(p1.firstName)
# print(p2.lastName)
# p1.fullName()
# print(p1.__dict__)  #it will give you the full description of your class as a dictinary

# class Circle:
#     pi=3.14 #class variables
#     temp=0
#     def __init__(self,radius):
#         Circle.temp+=1
#         self.radius=radius
#     def circumference(self):
#         print(self.radius*Circle.pi*2)
#     @classmethod  #class methods
#     def countOfObjects(cls):
#         print(cls.temp)

# c1=Circle(3)
# c2=Circle(3)
# c3=Circle(3)
# c4=Circle(3)
# c1.circumference()
# c1.countOfObjects()
# print(Circle.temp)
# Circle.countOfObjects() 

