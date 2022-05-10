squares=[i**2 for i in range(1,11)]
print(squares)

negetive=[-i for i in range(1,11)]
print(negetive)

names=["arnab","ambitama","suborno"]
firstLetter=[i[0] for i in names]
print(firstLetter)

strs=["abc","tuv","xyz"]
reveStrs=[i[::-1] for i in strs]
print(reveStrs)

evenNums=[i for i in range(1,11) if i%2==0]
print(evenNums)
oddNums=[i for i in range(1,11) if i%2!=0]
print(oddNums)

allLists=[1,2,3,1.2,1.5,"arnab","ambitama",["arnab","suborno"],[1,2,4,5],True,True,False,(1,2,3,4),(2,3,4,5),{"name":"arnab","songs":"tu jane na"},{"name":"arnab saha","songs":"tu jane na"}]

listList=[i for i in allLists if type(i)==list]
dictList=[i for i in allLists if type(i)==dict]
strList=[i for i in allLists if type(i)==str]
intList=[i for i in allLists if type(i)==int]
boolList=[i for i in allLists if type(i)==bool]
floatList=[i for i in allLists if type(i)==float]

print(listList)
print(dictList)
print(strList)
print(intList)
print(boolList)
print(floatList)

diffSeq=[-i if i%2!=0 else i*2 for i in range(1,11)]
print(diffSeq)

nestedComponent=[[i for i in range(1,4)] for j in range(3)]
print(nestedComponent)