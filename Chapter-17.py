def func:       #syntax error #when you write wrong syntax
    pass

if true:
print(arnab)     #indandation error  #when you messed up with spaces

print(name)        #name error   #when you use undeclared variable

print(8+"arnab")     #type Error    #when you messed up with different types

l=[1,2,3]           #index error    #when you use some index which are not present
print(l[8])

s="arnab"
print(int(s))        #value error     #when you put wrong value at wrong positions

l=[1,2]                 #attribute error    #when you use a attribute which is not build yet
l.push(1)

d={"arnab":"saha"}
print(d["age"])               #key error      #when you have used a undefined key in a dictionary

def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("sorry you are passing wrong data type to the function")
    
print(add("a",1))

class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError("you have to make a sound function in all of your subclass")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "bhow bhow"
    
doggy= Dog("oli","pug")
print(doggy.sound())


class Mobile:
    def __init__(self,name):
        self.name=name

class MobileStore:
    def __init__(self):
        self.store=[]
    def addPhone(self,newPhone):
        if isinstance(newPhone,Mobile):
            self.store.append(newPhone)
        else:
            raise TypeError("new mobile isn't in Mobile Class")

sumsang=Mobile("samsung galaxy s8")
mStrore=MobileStore()
mStrore.addPhone(sumsang)
print(mStrore.store)
while True:
    try:
        age=int(input("enter your age: "))
        # break
    except ValueError:
        print("invalid input... please type a integer value!!")
    except:
        print("unexcepted error...")
    else:
        if age>18:
            print("you can play")
        else:
            print("no you can't play")
    finally:
        print("hello world")

class NameTooShortError(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NameTooShortError("name is too short")
username=input("enter your name: ")
validate(username)
print(f"hello {username}")
import pdb

pdb.set_trace()
age=input("type your age: ")
print(age+5)