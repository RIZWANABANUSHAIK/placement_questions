from collections import Counter
str1=str(input())
final = Counter(str1)
print(final)
final = max(final, key=final.get)
print("The most frequent letter is, ", final)