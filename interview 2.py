#make zero value last
a=[2,4,0,5,2,0,6,0]
i=0
while i<len(a):
    if a[i]==0:
        a.append(a[i])
        a.remove(a[i])
    i=i+1
print(a)
