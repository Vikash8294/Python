
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

salary = int(input("salary:"))
tax = salary*(0.2,0.1) [salary>=5000]
print(tax)