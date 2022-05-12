# l=[1,2,3,4]  #iterable

# i= iter(l)  #iter() function to make any iterable to iterator
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

def num(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
for j in num(10):
    print(j)

