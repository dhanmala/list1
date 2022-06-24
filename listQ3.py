#num=[50,40,23,70,56,12,5,10,7]
#max=num[0]
#for a in num:
    #if a>max:
    #    max=a
#print("max value is:",max)        

a=[50,40,23,70,56,12,5,10,7]
i=0
s_max=a[0]
while i<len(a):
    if s_max<a[i-1]:
        s_max=a[i]
    i=i+1
print(s_max)        