listy=[12,"arnab",True,2.5,None]  #we make a list with [] 
print(listy)
print(listy[0])  #to get any element from a list
listy[0]="zero"  #it will change the element of zero position in this list
listy[0:]="zero" #it will destructure the string in from of list
listy[0:]=[1,3,5,6,8] #it will replace the array
print(listy)
fruits=[]
fruits.append("apple")
fruits.append("mango")
fruits.append("grapes")
print(fruits)

fruits1=["mango","apple"]
fruits2=["graphes","orange"]
fruits3=fruits1+fruits2  #general list concatination
print(fruits3)
fruits1.extend(fruits2)  #with extend method we change the first list
print(fruits1)

fruits1=["mango","apple"]
fruits1.insert(1,"naspati") 
print(fruits1)