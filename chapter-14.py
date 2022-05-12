# def square(a):
#     return a**2
# s=square
# print(s.__name__)
# print(square.__name__)
# print(s)
# print(square)
# print(square is s)

# def toPower(n):
#     def calcPower(i):
#         return i**n
#     return calcPower
# cube=toPower(3)
# squr=toPower(2)
# print(cube(4))
# print(squr(4))
# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         print(f"you are calling {wrapper_function.__name__} function")
#         print(wrapper_function.__doc__)
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function
# def func1(a,b):
#     """the function would take 2 parameters and add them"""
#     return a+b
# print(func1(7,8))
# import time
# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         t1=time.time()
#         returned_value = any_function(*args,**kwargs)
#         t2=time.time()
#         print(t2-t1)
#         return returned_value
#     return wrapper_function

# @decorator_function
# def func(a,b):
#     return a+b

# print(func(2,3))

# from functools import wraps
# def onlyIntAllowed(function):
#     wraps(function)
#     def wrapper_function(*args,**kwargs):
#         if all([type(i)==int for i in args]):
#             return function(*args,**kwargs)
#         print("invalid argument")
#     return wrapper_function

# @onlyIntAllowed
# def addAll(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(addAll(2,3,4,[1,2]))

