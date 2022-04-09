def recursion(n):
    if n == 1:
        print('1')
    else:
        recursion(n-1)
        print(n)
recursion(4)

# def powerOfTwo(n):
#     if n == 0:
#         return 1

        
#     else:
#         power = powerOfTwo(n-1)
#         return power *2
# print(powerOfTwo(3))

# def iterativePower(n):
#     i = 0
#     power = 0
#     while i<n:
#         power = power *2
#         i+=1
#     return power 

