#*****************************************RAndom PAssword generator in list************************************
# import random
# import string
# # print(string.ascii_letters)
# # print(string.digits)
# # print(string.punctuation)
# charValue = string.ascii_letters+string.digits+string.punctuation
# # print(random.choice(charValue))
# password =[]
# for i in range (12):
#     x = random.choice(charValue)
#     password.append(x)

    
# print(password)
# print(len(password))

#''''''''''''''''''''''''''''''''''''''''''********************************************************

#Random password generator 
import random
import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
charValue = string.ascii_letters+string.digits+string.punctuation
# print(random.choice(charValue))
pass_len=int(input("Enter the size of Required Random password"))
password =""
for i in range (pass_len):
    password =password+ random.choice(charValue)

    
print(f"Your",pass_len,"digit Random Password is :",password)


# li = []
# for i in range(5):
#     x = int(input("enter the number "))
#     li.append(x)
# print(li)