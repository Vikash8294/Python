import time
# def RunFor():
#     for i in range(0,500,1):
#         print(i)

# def RunWhile():
#     i = 0
#     while(i<500):
#         print(i)
#         i=i+1


# init = time.time()
# RunFor()
# t1 = (time.time() - init)
# init = time.time()
# RunWhile()
# t2 = (time.time()- init)

# print("For",t1)
# print("while ",t2)
t = time.localtime()
original = time.strftime("%y-%m-%d - %H-%M-%S",t)
print(original)