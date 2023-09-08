s=str(input())
letter=str(input())
count=0
for i in range(len(s)):
    if s[i]==letter :
        count+=1

print(count)