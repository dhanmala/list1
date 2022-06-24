num=int(input("enter binary number"))
sum=0
i=0
while num!=0:
    rev=num%10
    sum=sum+rev*pow(2,i)
    num=int(num//10)
    i=i+1
print("decimal number:",sum )    