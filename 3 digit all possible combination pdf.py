num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
list1=[]
list1.append(num1)
list1.append(num2)
list1.append(num3)
print(list1)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i!=j and j!=k and k!=i:
                print(list1[i],list1[j],list1[k])