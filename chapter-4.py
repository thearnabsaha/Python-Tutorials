def lastchar(a):
    return a[-1]
name=input("type your name here: ")
print(lastchar(name))

def isOddOrEven(a):
    if a%2==0:
        return "your number is even"
    else:
        return "your number is odd"
number=int(input("type any number: "))
print(isOddOrEven(number))


def isBig(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b:
        return c
    return b
num1=int(input("type a number: "))
num2=int(input("type a number: "))
num3=int(input("type a number: "))
print(isBig(num1,num2,num3))

def isBig(a,b):
    if a>b:
        return a
    return b

def isBigger(a,b,c):
    return isBig(isBig(a,b),c)
num1=int(input("type a number: "))
num2=int(input("type a number: "))
num3=int(input("type a number: "))
print(isBigger(num1,num2,num3))

def ispalindrome(a):
    if a[::-1]==a:
        return "yes it is a palindrome"
    return "no it's not a palindrome"
string=input("type a palindrome: ")
print(ispalindrome(string))

def fib(n):
    a=0
    b=1
    if n<=0:
        print("invalid")
    elif n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")
fib(20)

def bio(_name,_age=20):
    print(f"my name is {_name} and age is {_age}")
bio("arnab",40)

def fib(n):
    a=0
    b=1
    if n<=0:
        print("invalid")
    elif n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b, end=" ")
fib(10)