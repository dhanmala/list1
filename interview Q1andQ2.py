pets=["dog","cat","fish","fish","cat","cat","dog","fish","dog"]
char=input("enter character")
i=0
count=0
while i<len(pets):
    if pets[i]==char:
        count=count+1
    i=i+1
print(count)        