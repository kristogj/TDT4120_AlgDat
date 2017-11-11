

#X og Y er to sekvenser

def LCS(X,Y):
    m = len(X)
    n = len(Y)
    b = [[-1 for _ in range(m)] for _ in range(n)]
    c = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1,m):
        c[i][0] = 0
    for j in range(0,n):
        c[0][j] = 0
    for i in range(0,m):
        for j in range(0,n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = "UL"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "UP"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "LE"
    return c,b

c,b = LCS("ABCBDA","BDCABA")
str1 = ""
for line in c :
    str2 = ""
    for num in line:
        str2 += " " + str(num) + " "
    str1 += str2+"\n"
print(str1)

print()
for line in b :
    str2 = ""
    for num in line:
        str2 += " " + str(num) + " "
    str1 += str2+"\n"
print(str1)