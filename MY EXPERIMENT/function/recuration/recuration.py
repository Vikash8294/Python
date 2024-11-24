# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(7))
    
    
# def Sum(n):
#     if(n==0):
#         return 0
#     return Sum(n-1) + n
# sum = Sum(5)
# print(sum)

# def print_list(list,indx=0):
#     if (indx == len(list)):
#         return
#     print(list[indx])
#     print_list(list,indx+1)
# cities =["ara","biohar","khj","ch"]
# print_list(cities)
        
# cube = lambda x:x*x

# li = [ 1,2,3,4,5,6,7,8,9,10]
# res = list(map(cube,li))
# print(res)



def outer_function(a):
    def inner_function(b):
        return a*b
        
    return inner_function

closure = outer_function(5)
res = closure(3)
res2 = closure(5)
print (res2)
print(res)


# import time
# def ForLoop():
#     for i in range(0,500,1):
#         print(i)
        
# def WhileLoop():
#     i = 0
#     while i<500:
#         print(i)
#         i=i+1
    
# init = time.time()
# print(ForLoop())
# ForTime = time.time() - init
# init = time.time()
# print(WhileLoop())
# WhileTime = time.time() - init
# print (ForTime)
# print(WhileTime)

# import os
# if(not os.path.exists('data')):
#     os.mkdir('data')

# for i in range(0,100,1):
#     os.mkdir(f"data/day{i+1}")

        

#***********************
#***************1. Write a function to estimate polar coordinate of any point.
# def polar(p1):
    # x = p1["x"]
    # y = p1["y"]
    # r = (x**2+y**2)**(1/2)
    # phi = math.degree( math.atan2(y,x))
    # return(r,phi)
    
    # print(polar(p2))