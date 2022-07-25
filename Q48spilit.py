a=[12,45,23,67,78,90,45,32,100,76,38,62]
chunk_list=list()
chunk_size=4
for i in range(0,len(a),chunk_size):
    chunk_list.append(a[i:i+chunk_size])
print(chunk_list)    