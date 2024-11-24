# # #*************************************LIST**********************************
# # marks = [94.5,98.5,54,58,47,14]
# # print(marks)
# # print(type(marks))
# # print(marks[0],marks[-1])
# # print(len(marks))
# # print(marks[1:4])
# # print(marks[-3:-1])


# list=[3,2,1]
# print(list)
# list.append(4)
# print(list)
# list.sort() # accending order
# print(list)
# list.sort(reverse=True) #Decerasing order
# print(list)
# #it also sort string as per dictonary
# list.reverse()
# print(list)
# #************insert*****
# list.insert(1,5) #insert it does not delect the item
# print(list)

# #****************remove******
# list.remove(5) # remove item when it see the first time
# print(list)
# list.pop(2) #remove the element with index
# print(list)


#************************************************TUPLE******************************
# tup=(1,2,5,4,3,"voik",2)
# print(type(tup))
# print(tup[1:3])
# print(tup.index(5)) #important
# print(tup.count(2))

#**************pratice question ***********************
# flim1 =input("enter the 1 movie:")
# flim2 =input("enter the 1 movie:")
# flim3 =input("enter the 1 movie:")
# List=[]
# List.append(flim1)
# List.append(flim2)
# List.append(flim3)

# print(List)

#***********************Palindrome*******************************
List = []
List.append(input("enter the first number"))
List.append(input("enter the 2 number"))
List.append(input("enter the 3 number"))
print("the original list is :",List)
List_copy = List.copy()
List_copy.reverse()
if(List_copy == List):
    print("Palindrome")
else:
    print("not palindrome")



#******************************
# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)
# list.sort(reverse = True)
# print(list)