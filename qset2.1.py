a=[1,2,3,4,5]
b=[2,3,1,0,6,7]
x=len(a)
y=len(b)
for i in range(x):
    for j in range(y):
        if (a[i]==b[j]):
            break
        if (j==y-1):
            print(a[i],end=" ")
