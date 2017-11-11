
Inf = float(1e3000)
def matrix_multiply(A,B):
    if len(A[0]) != len(B):
        return "error - incompatible dimensions"
    else:
        C = [[0 for _ in range(len(A))] for _ in range(len(B[0]))]
        for i in range(0,len(A)):
            for j in range(0,len(B[0])):
                C[i][j] = 0
                for k in range(0,len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]
        return C


#p er en sekvens av matriser
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[-1 for _ in range(n)] for _ in range(n)]
    s = [[-1 for _ in range(n-1)] for _ in range(1,n)]
    for i in range(n):
        m[i][i] = 0
    for l in range(1,n):
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = Inf
            for k in range(i,j-1):         #?????????
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s

A= [[1,2,3],[1,2,3],[1,2,3]]
B = A

print(matrix_multiply(A,B))
