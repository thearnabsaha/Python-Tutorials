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
#         print("this is awesome function")
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function
# def func1(a):
#     print(f"this is the function 1 with argument {a}")
# func1(7)

# decorator_function(func1(7))

