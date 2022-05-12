l=[1,2,3,4]  #iterable

i= iter(l)  #iter() function to make any iterable to iterator
print(next(i))
print(next(i))
print(next(i))
print(next(i))

def num(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
for j in num(10):
    print(j)

square=(i**2 for i in range(1,11))

for i in square:
    print(i)
    
import time
t1=time.time()
square=[i**2 for i in range(1,10000000)]

for i in square:
    print(i)
t2=time.time()
square=(i**2 for i in range(1,10000000))

for i in square:
    print(i)
print(t2-t1)