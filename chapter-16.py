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
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def circumference(self):
#         print(self.radius*Circle.pi*2)

# c1=Circle(3)
# c1.circumference()

