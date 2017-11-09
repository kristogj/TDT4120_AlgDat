import time
#p liste av priser, n lengde tau
#Hvorfor funker ikke denne?..
def cut_rod(p,n):
    if n == 0:
        return 0
    q = -99999
    for i in range(1,n+1):
        q = max(q,p[i]+cut_rod(p,n-1))
    return q

def CUT_ROD(p, n):
    q = 0
    for i in range(1,n+1):
        q = max(q, p[i] + CUT_ROD(p, n - i))
    return q

###############################################

# Denne får samme problem som øverste cut-rod..
def memoized_cut_rod(p,n):
    r = [-9999]*(n+1)
    return memoized_cut_rod_aux(p,n,r)

def memoized_cut_rod_aux(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -9999
        for i in range(1,n+1):
            q = max(q,p[i] + memoized_cut_rod_aux(p,n-1,r))
    r[n] = q
    return q

def bottom_up_cut_rod(p,n):
    r = [0]*(n+1)
    for j in range(1,n+1):
        q = -9999
        for i in range(1,j+1):
            q = max(q,p[i] + r[j-i])
        r[j] = q
    return r[n]

def main():
    #pris for lengde 1,2,..,n
    priser = [0,4,9,15,18,21,28,31,37]
    n = 8

    print(cut_rod(priser,n))
    begin = time.time()
    print(CUT_ROD(priser,n))
    print("Total runtime: " + str(time.time() - begin))
    begin = time.time()
    print(bottom_up_cut_rod(priser,n))
    print("Total runtime: " + str(time.time() - begin))
main()
