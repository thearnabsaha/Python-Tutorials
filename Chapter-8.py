s1={1,2,3,4,3}
print(s1)

l=[1,2,3,4,3]
s2=set(l)
print(s2)

s3=list(set(l))
print(s3)

s1.add(4)
s1.add("arnab")
print(s1)

s1.remove(3)
print(s1)

s1.discard(9)
print(s1)

s1.clear()
print(s1)

sc=s1.copy()
print(sc)

for i in s2:
    print(i)
    
if 1 in s2:
    print("present")
else:
    print("not present")

unionSet=s1|s2
print(unionSet)
IntersectionSet=s1&s2
print(IntersectionSet)