str1=str(input())
mySet = set(str1)
for element in mySet:
    countOfChar = 0
    for character in str1:
        if character == element:
            countOfChar += 1
    print(element,countOfChar)
