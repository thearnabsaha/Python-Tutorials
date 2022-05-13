# def func:       #syntax error #when you write wrong syntax
#     pass

# if true:
# print(arnab)     #indandation error  #when you messed up with spaces

# print(name)        #name error   #when you use undeclared variable

# print(8+"arnab")     #type Error    #when you messed up with different types

# l=[1,2,3]           #index error    #when you use some index which are not present
# print(l[8])

# s="arnab"
# print(int(s))        #value error     #when you put wrong value at wrong positions

# l=[1,2]                 #attribute error    #when you use a attribute which is not build yet
# l.push(1)

# d={"arnab":"saha"}
# print(d["age"])               #key error      #when you have used a undefined key in a dictionary

# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError("sorry you are passing wrong data type to the function")
    
# print(add("a",1))

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         raise NotImplementedError("you have to make a sound function in all of your subclass")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed
#     def sound(self):
#         return "bhow bhow"
    
# doggy= Dog("oli","pug")
# print(doggy.sound())