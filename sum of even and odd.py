even_sum=0
odd_sum=0
n=int(input("enter number of element"))
for i in range(1,n+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("sum of even numbers=",even_sum)
print("sum of odd number=",odd_sum)            
        