#list1=[1,2,3,4,5,6,7,8]
#list2=[12,34,56,78]
#for x in list2:
#    list1.append(x)
#print(list1)    
list=["1","2","3","4","5","6","7","8"]
i=0
list1=[]
while i<len(list):
    b=list[i]+list[i+1]
    list1.append(b)
    i=i+2
print(list1)
