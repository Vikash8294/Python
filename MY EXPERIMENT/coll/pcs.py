#**************************1*********************Q1 Even or Odd (5 Marks)
#Write a Python function that iterates through the list and prints whether each number is even or odd.

def EvenOdd(list):
    for i in list:
        if(i%2==0):
            print("even")
        else:
            print("odd")
        

#number = [12,7,19,24,5,17,28,13]
#EvenOdd(number)

#***********************2********************
#Q2 Sum of Numbers (5 Marks)
#Using a while loop, write a Python program that calculates and prints the sum of all numbers in the list.


# number = [12,7,19,24,5,17,28,13]
# i = 0
# sum = 0
# print("the original List is")
# while i < len(number):
#     print(number[i])
    
#     sum= sum + number[i]
#     i = i+1
# print("The Sum of list is ",sum)



#*********************************3************
# Maximum and Minimum (5 Marks)
#Write a Python function find_max_min(numbers) that uses
# if-else statements to find and return the maximum and minimum numbers from the list

def find_max_min(numbers):
    min = numbers[0]
    max = numbers[0]
    for i in range(len(numbers)):
        if(min>numbers[i]):
            min = numbers[i]
        elif(max<numbers[i]):
            max = numbers[i]
    print(min)
    print(max)
# numbers = [12,7,19,24,5,17,28,13]
# find_max_min(numbers)


#***********Q4 Prime Numbers (5 Marks)
#Write a Python function find_primes(numbers) that uses a nested for loop and if-else statements to find and 
# return a list of prime numbers from the given list.
# n = 10
# for i in range(2,n,1):
#     if(n%i==0):
#         print("not prime")
#         break
#     else:
#         print("prime")
#         break





#*************************************Using function************************************
def find_prime(numbers):
    fact = 1
    for i in range(numbers,1,-1):
        fact = fact *i
        
    print(fact)
    
    # for i in range(len(numbers)):
    #     n = numbers[i]
    #     for j in range(2,n,1):
    #         if(n%j==0):
    #             print("Not Prime")
    #             break
    #         else:
    #             print("Prime")
    #             break
numbers = int(input("enter the no"))
find_prime(numbers)


