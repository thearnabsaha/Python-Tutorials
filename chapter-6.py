days=("sunday","monday","tuesday",'wednesday',"thursday","friday","saturday")
print(days)
for i in days:
    print(i)

num=(1,)
name=("arnab",)
name=()
print(type(name))

days2="sunday","monday","tuesday",'wednesday',"thursday","friday","saturday"
print(type(days2))

name1,name2=("arnab","suborno")
print(name2)

listInTuples = ('arnab',['suborno',"sohini"])
listInTuples[1].pop()
listInTuples[1].append("ambitamta")
print(listInTuples)

nums=(1,2,3,4,5,6)
print(min(nums))
print(max(nums))
print(sum(nums))

def func(a,b):
    add= a+b
    mult=a*b
    return add,mult
print(func(2,3))   #it returns a tuple so we have to unpack the tuple to get the individual value
add,mult= func(2,3)
print(add)
print(mult)

nums=tuple(range(1,11))
lnums=list(nums) #to make it a list
snums=str(nums)  #to make it a string
print(nums)
print(lnums)
print(snums)