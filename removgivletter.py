s=str(input())
res=s
rem=("a","e","i","o","u","A","E","I","O","U")
# remove_letter=str(input())
# res=s.replace(remove_letter ,"")
# print(res)
for i in res:
    if i in rem :
        res=res.replace(i,"")
    
print(res)
# input_string = "PrepInsta"
# result = input_string
# vowels = ('a', 'e', 'i', 'o', 'u')
# for x in input_string.lower():
#     if x in vowels:
#         result = result.replace(x, "")

# print('After removing vowels : ', result)