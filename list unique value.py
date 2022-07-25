num=[12,23,14,12]
i=0
num1=[]
while i<len(num):
    j=0
    count=0
    while j<len(num):
        if num[i]==num[j]:
            count+=1
            if count>=2:
                if num[i]in num1:
                    pass
            else:
                num1.append(num[0])
        j=j+1
    i=i+1
print(num1)                