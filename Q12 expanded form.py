num=int(input("enter expanded form number"))
res=[]
for index,digit in enumerate(str(num)[::-1]):
    if int(digit)!=0:
        res.append(digit+('0'*index))
        final='+'.join(reversed(res))
print(final)        