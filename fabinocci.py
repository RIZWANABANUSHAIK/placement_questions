# first,second=0,1
# n = int(input())
# for i in range(0,n):
#     if i<=1:
#         result=i
#     else:
#       result = first + second 
#       first = second
#       second = result
#     print(result)
first,second=0,1
n = int(input("please give a number for fibonacci series : "))
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("fibonacci series are : ") 
for i in range(0,n):
    print(fibonacci(i))
