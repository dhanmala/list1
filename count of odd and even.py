a=[]
size=int(input("enter element"))
for i in range(size):
    n=int(input("enter number"))
    a.append(n)
even=0
odd=0
for i in range(size):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("total even=",even,"total odd=",odd)                
