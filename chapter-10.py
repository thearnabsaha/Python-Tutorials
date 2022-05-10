squares={i:i**2 for i in range(1,11)}
print(squares)

name="arnab saha"
wordCounter={i:name.count(i) for i in name}
print(wordCounter)

oddEven={i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(oddEven)

s1={i for i in range(2,10)}
print(s1)

names=["arnab","ambitama","suborno"]
s2={i for i in names}
print(s2)