# name = "vikash"
# age = 21
# age2 = age
# a = None
# old = False
# print("my name is :",name)
# print("my age is :",age)
# print("my age is :",age2)
# print(type(name))
# print(type(age))
# print(type(name))
# print(type(a))
"""a = 1000
b =500
diff = b-a
print(diff)"""
#***************************for no input int ******************


# a = int(input("enter the first no:"))
# b = int (input("enter the second no:")) 
# print(a**b)  # here ** is a valid opertaor which means a to the power b
# c = type(b)
# print(c)

#***********************for name input only input *********************
# name = input('name :')
# print("your name is :"+name)

# def Fact(n):
#     if n== 0 :
#         return 1
#     else:
#         return n * Fact(n-1)
    
# print(Fact(1))

# def sum(a=2,b=3):
#     print(a+b)

# sum()

# def infs(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")

# infs(name = "vikash", age = 30, job = "onwer")

# def describe_person(**info):
#          for key, value in info.items():
#              print(f"{key}: {value}")
             
# describe_person(name="Alice", age=30, job="Engineer")

# even = lambda x : x%2==0

# li = [ 1,2,3,4,5,6,7,8,9,10]
# res = list(filter(even,li))
# print (res)

# even = lambda x : x**2

# li = [ 1,2,3,4,5,6,7,8,9,10]
# res = list(map(even,li))
# print (res)

# square = [x**2 for x in range(5)]
# print(square)

# import time 
# def forloop():
#     for i in range(0,500,1):
#         print(i)
# def whileLoop():
#     i = 0
#     while(i<500):
#         print(i)
#         i = i+1
        
        
        
# init = time .time()
# whileLoop()
# t1 = time.time() - init
# init = time . time()
# forloop()
# t2 = time . time()- init
# print(t1)
# print(t2)

# s = [1,2,3]
# print(s.count(3))
# print(s)
# s = "vikashks Kumars"
# print(s.capitalize())

list = [1,2,3,4,5]
sum = 0
for i in range(len(list)):
    sum = sum + list[i]
print(sum)
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if (list[j] >list[i]):
#             temp = list[i]
#             list[i] = list[j]
#             list[j]= temp
#     print(list[i])     