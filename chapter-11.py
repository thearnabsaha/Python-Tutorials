def allSum(*args):
    total=0
    for i in args:
        total+=i
    return total
print(allSum(1,22,3))

def allmult(a,*args):
    total=1
    print(a)
    for i in args:
        total*=i
    return total
print(allmult(2,3,4))