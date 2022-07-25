list=[1,2,3,1,2,2]
res=[]
i=0
while i<len(list):
    if list[i] not in res:
        res.append(list[i])
    i=i+1
print("list after remove duplicates:",res)        
