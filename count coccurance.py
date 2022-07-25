string=["a","n","t","a","a","t","n","n","a","x","u","a","g"]
char=input("enter character")
i=0
count=0
while i<len(string):
    if string[i]==char:
        count+=1
    i+=1
print("total number of count",char,"is",count)        