def findMissing(a, b, n, m):
    for i in range(n):
        for j in range(m):
            if (a[i] == b[j]):
                break
        if (j == m - 1):
            print(a[i], end = " ")
 
if __name__ == "__main__": 
    a = [1,2,3,4,5,6]
    b = [2,3,1,0,6,7]
    n = len(a)
    m = len(b)
    findMissing(a, b, n, m)
