user1={'name':"arnab","age":20}
print(user1)
user2=dict(name="suborno",age=20)
print(user2)

print(user1["name"])

user3={}
user3["name"]="ambitama"
user3["age"]=21
print(user3)


if "name" in user1:
    print("present")
else:
    print("not present")
    
if "arnab" in user1.values():
    print("present")
else:
    print("not present")

for i in user1:
    print(i)
    
for i in user1.values():
    print(i)
    
print(user1.keys())
print(type(user1.keys()))  #dict keys
print(user1.values())
print(type(user1.values()))  #dict values
print(user1.items())
print(type(user1.items()))  #dict items

for keys,values in user1.items():
    print(f"key is {keys} and values is {values}")
    
user1["pokemon"]="keldeo"
print(user1)

popped_item=user1.pop("age")   #you are choosing which item to pop
print(popped_item)
print(user1)

popped_item=user1.popitem()    #you are popping the last item
print(popped_item)
print(user1)