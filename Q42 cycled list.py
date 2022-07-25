string_list=["a","b","c","d","e","f","g","h"]
i=0
k=3
res=[]
while i<len(string_list):
    if string_list[i]not in res:
        res.append(string_list[k%len(string_list)])
        k=k+1
    i=i+1
print("the cycled list is:",res)  
