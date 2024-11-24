# f = open("hello.py","r")
# line = f.read()
# data = f.readline(1)
# print(line)
# print(data)
# print(type(data))
# f.close()

# f = open("I\o file\om.txt","w")
# f.write("I am A good boy")
# f.close()
# f = open("I\o file\om.txt", "a")
# f.write("\nI am a lol boy")
# f.close()

# f = open("I\o file\om.txt","r+")
# f.write("addc")
# data = f.read()
# print(data)
# f.close()

# with open("pratice.txt","r") as f:
#     data = f.read()
#     print(data)
# new = data.replace("java","python")
# print(new)


# word = "learning"
# with open ("pratice.txt","r") as f :
#     data = f.read()
#     if (data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")
    
word = "java"
line = 1
data = True
with open ("pratice.txt","r") as f :
    while data :
        data= f.readline()
        if(word in data):
            print(line)
        line = line+1

  

    