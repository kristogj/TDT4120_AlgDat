
Inf = float(1e3000)


#P = liste over priser for lengde lik indeksen
#n = lengden av tauet
def cut_rod(P,n):
    if n == 0:
        return 0
    q = -Inf
    for i in range(1,n+1):
        s = cut_rod(P,n-i)
        q = max(q,P[i] + s)

    return q

def Memoized_Cut_Rod(p,n):
    r = [-Inf]*(n+1) #Må ha +1 pga første elementet vi har i listen vår er prisen for lengde 0 som er 0
    return Memoized_Cut_Rod_Aux(p,n,r)

def Memoized_Cut_Rod_Aux(p,n,r):
    if r[n] >= 0: #Sjekker om prisen for en hvis lengde er kjent fra før av
        return r[n] #riktig pga kjente priser er alltid større enn 0
    if n == 0: #Neste linjene gjøres på vanlig måte
        q = 0
    else:
        q = -Inf
        for i in range(1,n+1):
            q = max(q,p[i] + Memoized_Cut_Rod_Aux(p,n-i,r))
    r[n] = q #Lagres verdien til senere bruk
    print(r)
    return q

#Noe er galt..
def Buttom_Up_Cut_Rod(p,n):
    r = [-Inf]*(n+1)
    r[0] = 0
    for j in range(1,n+1):
        q = -Inf
        for i in range(1,j+1):
            q = max(q,p[i]+r[j-i])
        r[j] = q
        print(r)
    return r[n]

def Extended_Buttom_Up_Cut_Rod(p,n):
    r = [-Inf] * (n + 1)
    s = [-Inf] * (n + 1)
    r[0] = 0
    for j in range(1,n+1):
        q = -Inf
        for i in range(1,j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return r,s

def Print_CR(p,n):
    (r,s) = Extended_Buttom_Up_Cut_Rod(p,n)
    while n > 0:
        print(s[n],end=",")
        n = n - s[n]

priser = [0,1,2,4,2,2,2]
n = 6
print(cut_rod(priser,n))
print(Memoized_Cut_Rod(priser,n))
print(Buttom_Up_Cut_Rod(priser,n))
print("hei")
Print_CR(priser,n)


