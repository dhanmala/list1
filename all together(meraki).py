#all together.count,sum,average of even number and odd number
a=[23,14,56,12,19,9,15,25,31,42,43]
count_even=0
count_odd=0
i=0
while i<len(a):
    if a[i]%2==0:
        count_even+=1
    else:
        count_odd+=1
    i=i+1
print("count of even",count_even) 
print("count of odd",count_odd)          

a=[23,14,56,12,19,9,15,25,31,42,43]
count_even=0
count_odd=0
sum_even=0
sum_odd=0
i=0
while i<len(a):
    if a[i]%2==0:
       sum_even+=a[i]
       count_even+=1
    else:
        sum_odd+=a[i]
        count_odd+=1
    i=i+1
print(len(a))
print(sum(a))
avg1=sum_even/i
avg2=sum_odd/i
print("even number",count_even,sum_even,avg1)
print("odd number",count_odd,sum_odd,avg2)        
