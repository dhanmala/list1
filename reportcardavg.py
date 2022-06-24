number=30
sum=0
n=[10,11,12,13,14,17,18,19]
a=len(n)
for i in range(0,a):
    for j in range(i+1,a):
        if n[i]+n[j]==sum:
            number+=number
    print(n)        