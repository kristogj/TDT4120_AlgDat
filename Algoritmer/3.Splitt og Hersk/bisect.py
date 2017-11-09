
#A er en sortert liste
    #p = indeksen til første element
    #r = indeksen til siste element
    #v = verdien til det elementet vi vil finne indeksen til

def bisect(A,p,r,v):
    i = p
    if p < r:
        q = int((p+r)/2) #Finner indeksen til det miderste elementet
        if v <= A[q]: #Er v mindre eller lik det miderste elementet?
            i = bisect(A,p,q,v) # Del listen i 2 fra det nederste til midten
        else:
            i = bisect(A,q+1,r,v) # Del listen i 2 fra det miderste til det øverste
    return i

def bisect_merket(A,p,r,v):
    while p < r:
        q = int((p+r)/2)
        if v <= A[q]:
            r = q
        else:
            p = q + 1
    return p

A = [1,2,3,4,5,6,7,8,9]
print(bisect(A,0,len(A)-1,4))
print(bisect_merket(A,0,len(A)-1,4))
