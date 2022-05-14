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

# with open("file.txt","w") as f:
#     f.write("i am a pokemon") #it overwites the actual content of the file.
    
# with open("file.txt","a") as f:
#     f.write("i am a pokemon yeash") #it apprnds data at the end of the actual file.

# with open("file.txt","r+") as f: #it can read and write data together
#     f.seek(len(f.read()))
#     f.write("i am a pokemon yeash")
#     f.seek(0)
#     print(f.read())

# with open("file.txt") as rf:
#     with open("file2.txt","w") as wf:
#         wf.write(rf.read())

# with open("file.txt") as rf:
#     with open("file2.txt","w") as wf:
#         for line in rf.readlines():
#             name,age=line.split(",")
#             wf.write(f"{name}:{age}")

# with open("index.html","r") as rf:
#     with open("file.txt","w") as wf:
#         for line in rf.readlines():
#             if "<a href=" in line:
#                 pos=line.find("<a href=")
#                 first_qoute= line.find('\"',pos)
#                 second_qoute=line.find('\"',first_qoute+1)
#                 url=line[first_qoute+1:second_qoute]
#                 wf.write(url+"\n")