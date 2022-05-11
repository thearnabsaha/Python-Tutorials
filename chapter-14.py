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

# def decorator_function(any_function):
#     def wrapper_function():
#         print("this is awesome function")
#         any_function()
#     return wrapper_function

# @decorator_function
# def func1():
#     print("this is the function 1")
# func1()

# decorator_function(func1())