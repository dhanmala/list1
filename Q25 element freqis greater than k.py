test_list=[4,6,4,3,3,4,3,4,3,8]
k=2
i=0
res=[]
while i<len(test_list):
    count=0
    freq=test_list.count(i)
    if freq>k and i not in res:
        res.append(i)
    i=i+1
    count=count+1
print("required element:",res)        