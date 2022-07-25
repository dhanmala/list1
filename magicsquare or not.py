a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(a):
    s=0
    j=0
    while j<len(a[i]):
        s=s+a[i]
        j+=1
    i+=1
    print(a)
x=0
while x<len(a):
    s1=0
    y=0
    while y<len(a[x]):
        s1=s1+a[x][y]
        y=y+1
    x+=1
    print(s1,end="")
print()
if s==s1:
    print("magic square") 
else:
    print("not magic square")             