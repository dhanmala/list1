original_list=[5,6,[],3,[],[],9]
new_list=[]
for i in original_list:
    if i!=[]:
        new_list.append(i)
    else:
        continue
print(new_list)        