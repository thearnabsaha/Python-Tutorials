# for i,j in enumerate(names):
#     print(f"position:{i}---->value:{j}")

# names=["arnab","suborno","ambitama"]
# def func1(a,b):
#     for i,j in enumerate(a):
#         if j==b:
#             return i
#     return -1

# print(func1(names,"ambitamas"))

# nums=[1,2,3,4,5]
# print(list(map(lambda a:a**2,nums)))

# nums=[1,2,3,4,5]
# print(list(filter(lambda a:a%2==0,nums)))

# name=["arnab","ambitama","suborno","arijit","sayan"]
# nums=[1,2,3,4,5]
# print(list(zip(nums,name)))
# print(dict(zip(nums,name))) #cause we can change [(a,b),(c,d)] this kind of values to tuples but not the [(a,b,c),(d,e,f)] of value

# zippedList=[(1,2),(3,4),(5,6),(7,8),(9,0)]
# l1,l2=list(zip(*zippedList))
# print(list(l1))
# print(list(l2))