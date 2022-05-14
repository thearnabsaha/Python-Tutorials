# f=open("file.txt") #to open the the file
# print(f"cursor position: {f.tell()}") #to tell the position of the cursor
# print(f.read()) #to read the file
# print(f"cursor position: {f.tell()}")
# f.seek(0) #to change cursor's position to 0
# print(f"cursor position: {f.tell()}")
# print(f.readline()) #will read only one line
# f.seek(0) 
# lines=f.readlines()
# print(len(lines))
# for i in lines:
#     print(i)
# print(f.name)
# print(f.closed)
# f.close() 

with open("file.txt","w") as f:
    f.write("i am a pokemon")
    
with open("file.txt","a") as f:
    f.write("i am a pokemon yeash")

with open("file.txt","r+") as f:
    f.seek(len(f.read()))
    f.write("i am a pokemon yeash")
    f.seek(0)
    print(f.read())

