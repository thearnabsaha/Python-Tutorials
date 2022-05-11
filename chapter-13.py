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

# l1=[1,2,3]
# l2=[4,4,3]
# l3=[1,5,3]
# l4=[6,2,3]

# print(list(map(lambda a:sum(a)/len(a),zip(l1,l2,l3,l4))))

# l1=[1,2,3,4,5,6]
# l2=[2,4,6,8,10]

# print(all([i%2==0 for i in l2]))
# print(all([i%2==0 for i in l1]))
# print(any([i%2==0 for i in l1]))

# names=["arnab saha","suborno das","arnab","suborno"]
# print(max(names,key=lambda a:len(a)))
# print(min(names,key=lambda a:len(a)))

# students=[
#     {"name":"arnab saha","age":20,"score":97},
#     {"name":"suborno","age":22,"score":93},
#     {"name":"ambitama","age":21,"score":92},
#     {"name":"arijit","age":24,"score":91},
# ]

# print(max(students,key=lambda a:a.get("score")).get("name"))

# l1=["arnab","ambitama","suborno","arijit"]
# print(sorted(l1))

# s1={"arnab","ambitama","suborno","arijit"}
# print(sorted(s1))

# t1=("arnab","ambitama","suborno","arijit")
# print(sorted(t1))

# students=[
#     {"name":"arnab saha","age":20,"score":97},
#     {"name":"suborno","age":22,"score":93},
#     {"name":"ambitama","age":21,"score":92},
#     {"name":"arijit","age":24,"score":91},
# ]
# lowToHigh=sorted(students,key=lambda a:a.get("score"))
# highToLow=sorted(students,key=lambda a:a.get("score"),reverse=True)

# print(highToLow)
# print(lowToHigh)