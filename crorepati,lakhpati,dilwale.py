money=[3000,60000,324990909,90990900,30000,5600000,690909090,310101019,532010,510,4100]
count_crorepati=0
count_lakhpati=0
count_dilwale=0
i=0
while i<len(money):
    if money[i]>=100000000:
        count_crorepati+=1
    elif money[i]>=10000000:
        count_lakhpati+=1
    else:
        count_dilwale+=1
    i=i+1
print(count_crorepati,"crorepati")                
print(count_lakhpati,"lakhpati")
print(count_dilwale,"dilwale")