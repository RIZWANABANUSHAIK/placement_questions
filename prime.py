# num=int(input())
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    for i in range(2,int(num/2)+1):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")
#inbetween range
lower=int(input())
upper=int(input())
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,int(num/2+1)):
            if( num%i)==0:
                break
        else:
            print(num)
