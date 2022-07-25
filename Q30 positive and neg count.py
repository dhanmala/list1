list1=[20,24,-7,-27,-45,7,21]
pos_count=0
neg_count=0
i=0
while i<len(list1):
    if list1[i]>=0:
        pos_count+=1
    else:
        neg_count+=1
    i=i+1
print("positive number in list:",pos_count)
print("negative number in list:",neg_count)            
