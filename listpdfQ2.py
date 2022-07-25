a=[['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
c=()
for i in a:
    for j in i:
        j.join(c)
        print(j,end="")
    