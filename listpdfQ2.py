name_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
res = ''.join(ele for sub in name_list for ele in sub)
print("The String after join : " + res) 