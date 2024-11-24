# def prime(numbers):
#     print("The list of prime numbers are:")
#     for i in range(len(numbers)):
#         n = numbers[i]
#         for j in range(2,n,1):
#             if (n%j==0):
#                 print(n)
#                 break
# numbers = [12,7,19,24,5,17,28,13]
# prime(numbers)


#lamda map filter
# def cube(x):
#     return x*x*x
# cube = lambda x: x*x*x

# l =[1,2,3,6]
# # newl = list(map(cube,l))
# # print(newl)
# def filter_function(a):
#     return a>2

# l =[1,2,3,6]
# newl = list(filter(filter_function,l))
# print(newl)

#closure
def outer_fun(a):
    def inner_fun(b):
        return a*b
    
    return inner_fun
closure = outer_fun(5)
res = closure(3)
res1 = closure(4)
print(res)
print(res1)