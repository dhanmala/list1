binary_number=[1,0,0,11,0,1,1] 
bin=[1,1,0,1,1,0,0,1]#backward
i=0
dec=0
while i<len(bin):
    if bin[i]==1:
        dec=dec+2**i
    i=i+1
print(dec)    
