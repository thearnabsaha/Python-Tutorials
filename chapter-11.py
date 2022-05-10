# def allSum(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(allSum(1,22,3))

# def allmult(a,*args):
#     total=1
#     print(a)
#     for i in args:
#         total*=i
#     return total

# nums1=[2,4,5,6]
# nums2=(2,4,5,6)
# print(allmult(2,*nums1))
# print(allmult(2,*nums2))


# def func1(**kwargs):
#     print(kwargs)
# func1(name="arnab",age=20)

# def func2(**kwargs):
#     for i,j in kwargs.items():
#         print(f'{i}:{j}')
# func2(name="arnab",age=20)

# def func3(pokemon,**kwargs):
#     for i,j in kwargs.items():
#         print(f'{i}:{j}:{pokemon}')
# func3("keldeo",name="arnab",age=20)

# def func4(pokemon,**kwargs):
#     for i,j in kwargs.items():
#         print(f'{i}:{j}:{pokemon}')
# d={"name":"arnab","age":20}
# func4("keldeo",**d)

# def func(name,*args,lastName="unknown",**kwargs):
#     print(name)
#     print(args)
#     print(lastName)
#     print(kwargs)
# func("arnab",1,2,3,pokemon="keldeo")
# func("arnab",1,2,3,lastName="saha",pokemon="keldeo")

# def func(a,**kwargs):
#     if kwargs.get("reversed")==True:
#         print([i[::-1].title() for i in a])
#     else:
#         print([i.title() for i in a])
# names=["arnab","ambitama"]
# func(names,reversed=True)
# func(names)