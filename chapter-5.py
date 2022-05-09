# listy=[12,"arnab",True,2.5,None]  #we make a list with [] 
# print(listy)
# print(listy[0])  #to get any element from a list
# listy[0]="zero"  #it will change the element of zero position in this list
# listy[0:]="zero" #it will destructure the string in from of list
# listy[0:]=[1,3,5,6,8] #it will replace the array
# print(listy)
# fruits=[]
# fruits.append("apple")
# fruits.append("mango")
# fruits.append("grapes")
# print(fruits)

# fruits1=["mango","apple"]
# fruits2=["graphes","orange"]
# fruits3=fruits1+fruits2  #general list concatination
# print(fruits3)
# fruits1.extend(fruits2)  #with extend method we change the first list
# print(fruits1)

# fruits1=["mango","apple"]
# fruits1.insert(1,"naspati") 
# print(fruits1)


# name=["arnab","ambi","suborno","samriddhi","arijit"]
# name.pop() #it will delete last element
# name.pop(1) #it will delete 1 placed element

# del name[0] #it will delete 0 placed element

# name.remove("samriddhi") #it will delete this item from the list. if it os present more than one times it will only delete one item like this

# print(name)

# name=["arnab","ambi","suborno","samriddhi","arijit"]
# if "arnab" in name:
#     print("is present")
# else:
#     print("not presernt")
# print(name.count("arnab")) #how many times is the item available
# name.sort() #to sort the origianl array alphabetically
# print(name)

# numbers=[3,6,8,1,5,7,9,12,67]
# numbers.sort()  #to sort the original array numerically
# print(numbers)
# print(sorted(numbers)) #it will not sort the origianl array
# numbers.clear() #to clear the array
# print(numbers)
# numbersCopy=numbers.copy() #to get a copy of the array
# print(numbersCopy)

# name1=["arnab","ambi","suborno","samriddhi","arijit"]
# name2=["arnab","ambi","suborno","samriddhi","arijit"]

# print(name1==name2) #True #checks the value
# print(name1 is name2) #False #checks the memory allocation

# name="arnab ambi arijit".split(" ") #.split() method breaks strings into list
# print(name)
# name=["arnab","20","arijit"]

# print(",".join(name)) #.join() method add lists to a string


# name=["arnab","ambi","suborno","samriddhi","arijit"]

# for i in name:
#     print(i)

# i=0
# while i<len(name):
#     print(name[i])
#     i+=1

# matrix=[[1,2,3],[4,5,6],[7,8,9]] #2d matrix == list inside list
# print(matrix[2])
# print(matrix[1][2])
# for i in matrix:
#     for j in i:
#         print(j)
# print(type(matrix)) #what kind of data type is this

# numbers= list(range(1,11)) #by this we make a list with range
# print(numbers)

# print(numbers.index(1)) #array.index(the item we are finding,from this range, to that range)

# # we can pass list in a function also 
# def negativeList(l):
#     negative=[]
#     for k in l:
#         negative.append(-k)
#     return negative
# print(negativeList(list(range(1,11))))

# def sqr(l):
#     sqlist=[]
#     for i in l:
#         sqlist.append(i**2)
#     return sqlist
# print(sqr(list(range(5,17,2))))

# def rev(l):
#     l.reverse()
#     return l
# nums=[1,2,3,4,5,6,7,8,9]
# print(rev(nums))

# def rev(l):
#     return l[::-1]
# nums=[1,2,3,4,5,6,7,8,9]
# print(rev(nums))

# def rev(l):
#     revlist=[]
#     for i in range(0,len(l)):
#         revlist.append(l.pop())
#     return revlist
# nums=[1,2,3,4,5,6,7,8,9]
# print(rev(nums))

# names=["arnab","ambitama","suborno","arijit"]
# def rev(l):
#     revstring=[]
#     for i in l:
#         revstring.append(i[::-1])
#     return revstring

# print(rev(names))

