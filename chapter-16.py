class Person:
    def __init__(self,firstName,lastName,age):
        #instance Variables
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        
p1=Person("arnab","saha",20)
p2=Person("ambitama","saha",21)
print(p1.age)
print(p2.firstName+" "+p2.lastName)