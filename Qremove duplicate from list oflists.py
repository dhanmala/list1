list=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
new_list=[]
i=0
while i<len(list):
    if list[i] not in new_list:
        new_list.append(list[i])
    i=i+1
print("new list:",new_list)
