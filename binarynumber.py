num=int(input())
res= set(list(map(int, str(num))))
binary={0,1}
result = res.difference(binary)
if len(result)==0:
    print("given number is binary")
else:
    print("not binary")
