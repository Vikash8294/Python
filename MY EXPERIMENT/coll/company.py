# Question:
# A company wants to create a utility program that helps employees track their monthly expenses. 
# You are tasked with writing a Python program that includes several functions to calculate 
# different aspects of the expenses. Answer the following sub-questions:

# a) Define a function calculate_total_expenses() that takes a list of expenses (integers or floats) 
# as input and returns the total sum of expenses.
# (5 Marks)

def calculate_total_expenses(list):
    sum = 0
    print("Expenses Are ")
    for i in range(len(list)):
        print(list[i])
        sum = sum + list[i]
    print("the sum of expenses are ",sum)
# list = []
# while True:
#     exp = int(input("enter your expenses "))
#     list.append(exp)
#     choice = input("press n to stop and y to continue ")
#     if(choice.casefold() == "n"):
#         break


# calculate_total_expenses(list)


#**********************************
# b) Define a function calculate_average_expense() that calculates the average expense from a list of expenses. 
# Make sure to handle cases where the list might be empty.
# (5 Marks)
def calculate_average_expense(list):
    sum = 0
    for i in range(len(list)):
        sum = sum +list[i]
        avg = sum/len(list)
        
    print("The average expense is :",avg)


# list=[]
# while True:
#     choice = input("enter y / n")
#     if(choice.casefold() == "n"):
#         break 
#     exp = float(input("enter your expenses : "))
#     list.append(exp)
    
# calculate_average_expense(list)


#**************************************
# c) Write a function find_maximum_expense() that takes a list of expenses and 
# returns the highest expense. Ensure you handle the case when the list is empty by returning None.
# (5 Marks)

def find_maximum_expense(list):
    max = list[0]
    for i in range(len(list)):
        if (max<list[i]):
            max = list[i]
    print("The max expense is : ",max)
        



list = []
while True:
    choice = input("Y/N : ")
    if ( choice.casefold()== "n"):
        break
    exp = float(input("enter the expense"))
    list.append(exp)
    
find_maximum_expense(list)



    