number=30
n=[10,11,12,13,14,17,18,19]
i=0
b=[]
while i<len(n):
    c=[]
    j=i+1
    while i<len(n):
        a=n[i]+n[j]
        if a==30:
            a=n[i]+n[j]
            c.append(n[i])
            c.append(n[j])
            b.append(c)
        j=j+1
    i=i+1
print(b)            