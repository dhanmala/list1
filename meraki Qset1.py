#count element
num_list=[50,40,10,70,56,12,5,10]
x=10
count=0
for ele in num_list:
    if ele==x:
        count=count+1
print("{} has occured {} times".format(x,count))        
