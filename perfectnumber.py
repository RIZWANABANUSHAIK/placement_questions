num=int(input())
sum=0
for i in range(1,int(num/2)+1):
    if (num%i)==0:
        sum=sum+i

if sum == num :
    print("it is perfect")
else:
    print("not")
    