n=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
m=1
min=1
while i<len(n):
    j=0
    while j<len(n[i]):
        p=len(n[i])
        if p>=m:
            m=p
            max=n[i]
        if p<=min:
            min=p
            minimum=n[i]
        j=j+1
    i=i+1            
print("list maximum length:",m,max)
print("list minimum length:",min,minimum)            
