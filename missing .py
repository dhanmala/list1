list = [0,1,2,4,5]
missing=[]
for i in range(list[0],list[-1]+1):
    if i not in list:
        missing.append(i)
print(missing)
