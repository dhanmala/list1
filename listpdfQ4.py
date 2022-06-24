list=[6,1,3,5,6,3,1]
i=0
list1=[]
while i<len(list):
    if list[i] not in list1:
        list1.append(list[i])
        i=i+1
        print(list1)    
