list=['Red','Maroon','Yellow','Olive']
i=0
l=[]
while i<len(list):
    j=0
    c=[]
    while j<len(list[i]):
        c.append(list[i][j])
        j=j+1
    i=i+1
    l.append(c)
print(l)
