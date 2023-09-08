a = int(input(" "))
b = int(input(" "))
a=a-b
b=a+b
a=b-a
print("value of a is : ", a);
print("value of b is : ", b); 

#with 3rd variable
a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
tempvar=a
a=b
b=tempvar
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b); 