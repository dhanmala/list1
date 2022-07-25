# Python3 code to demonstrate working of
# Scramble strings in list
# using list comprehension + sample() + join()
#from random import sample 
  
# initialize list 
#test_list = ['gfg', 'is', 'best', 'for', 'geeks']
  
# printing original list 
#print("The original list : " + str(test_list))
  
# Scramble strings in list
# using list comprehension + sample() + join()
#res = [''.join(sample(ele, len(ele))) for ele in test_list]
  
# printing result
#print("Scrambled strings in lists are : " + str(res))

list=[4,6,4,3,3,4,3,4,3,8]
k=2
i=0
res=[]
while i<len(list):
    count=0
    freq=list.count(i)
    if freq>k and i not in res:
        res.append(i)
    i=i+1
    count=count+1
print("required element:",res)        