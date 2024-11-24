
#**********************************conditional statement for traffic light***************************************

# color =input("enter traffic color :")
# if(color == "red"):
#     print("STOP")
# elif(color == "yellow"):
#     print("WAIT")
# elif(color == "green"):
#     print("GO")
# else:
#     print("LIGHT IS BROKEN")



#*********************************************conditional statement for Grade system**********************************

# marks =int(input("enter your marks :"))
# if(marks >=90 and marks <= 100):
#     print("A")
# elif(marks>=80 and marks <= 89):
#     print("B")
# elif(marks >=70 and marks <=78):
#     print("C")
# else:
#     print("D")


#******************************if else in one line **********************************
# food = input("rnter the food:")
# eat = "yes" if food == "cake" else "no"
# print(eat)
              #********************Single line ifOR****************
              
# food = input("enter food:")  
# print("sweet") if food == "jalebii" or food == "mitia" else print("not sweet")           
#*********************cleverif ternary operator*****************
# age = int(input("AGE:"))
# vote = ("no", "yes")[age>=18]
# print(vote)

# salary = int(input("salary:"))
# tax = salary*(0.2,0.1) [salary>=5000]
# print(tax)


#***********************prtaice quetsion***********************
# num1 = int(input("Enter the Number"))
# if(num1%2==0):
#     print("Even")
# else:
#     print("Odd")


#*****************************************************************************
# num1 = int(input("Enter the 1 Number"))
# num2 = int(input("Enter the 2 Number"))
# num3 = int(input("Enter the 3 Number"))
# num4 = int(input("Enter the 4 Number"))
# if(num1>num2 and num1>num3 and num1>num4):
#     print("GREATEST IS :",num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("GREATEST IS :",num2)
# elif(num3>num1 and num3>num2 and num3>num4):
#     print("GREATEST IS :",num3)
# else:
#     print("GREATEST IS:",num4)


num1 = int(input("Enter the Number"))
if(num1%7==0):
    print(num1,"is multiple of 7")
else:
    print(num1,"is not a multiple of 7")