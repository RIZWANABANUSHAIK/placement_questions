vowel=["a","e","i","o","u"]
str1=str(input())
str1=str1.lower()
str1=set(str1)
vowels=0
conson=0
for i in str1:
    if i in vowel :
        vowels+=1
    else:
        conson+=1

print(vowels,conson)
