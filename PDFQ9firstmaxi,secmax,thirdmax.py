n=[1,27,14,2,41,58,94,87]
i=0
max=0
s_max=0
third_max=0
while i<len(n):
    if n[i]>max:
        third_max=s_max
        s_max=max
        max=n[i]
    elif n[i]>s_max:
        third_max=s_max
        s_max=n[i]
    elif n[i]>third_max:
        third_max=n[i]
    i=i+1
print("first maximum is:",max)
print("second maximum is:",s_max) 
print("third maximum is:",third_max)       


