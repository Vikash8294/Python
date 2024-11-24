# x = 1
# while x <=5 :
#     print("hello")
#     x=x+1
# print(x)    
    
    
# i=0 
# x=(1,4,9,16,25,36,49,64,81,100)
# y = 16
# while i<+len(x):
#     print(x[i])
#     if x[i]==y:
#         print("Found at index",i)
#         break;
    
#     i += 1
# print("end of loop")
#**********************************************
#using for loop binary search*********************************

# x=[1,4,9,16,25,36,49,64,81,100]
# y = 16
# idx = 0
# for i in x:
#     if (i == y):
#         print("Found at",idx)
#     idx +=1
    
    
    
#     i = i+1

# list=[]
# i = 1
# while i < 5:
#     list.append(input("enter the element"))
    
    
    
#     i = i+1

    
# print(list)

#**********************************************************************

# s = "vikash"
# for i in s:
#     print(i)
#     if i == "k" :
#         print("found")
#         break

 #******************************************
 # range ******************************************************
# seq = range(5)  
# print(seq[0]) 
# print(seq[1]) 
# print(seq[2]) 
# print(seq[3]) 
# print(seq[4]) 

#*******************sum of first natural no. using while**********
# n = int (input("enter the number "))
# i =0
# sum = 0
# while i <= n:
#     sum = sum+i
#     i = i+1
# print(sum)


#*************************Factorial *************
n = int (input("enter the number "))
factorial = 1
for i in range(n,1,-1):
    factorial = factorial*i
print(factorial)
    