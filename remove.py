list=[2,3,4,5,6,5,9,5]
res=5
for i in list:
    if i==res:
        list.remove(res)
print(list)
