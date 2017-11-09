from random import randint
from time import time
#A = liste
#p = laveste index
#r = høyeste index
#i er det i minste elementet i listen vi vil finne. Hvor i=1 vil si det minste

def randomized_select(A,p,r,i):
    if p == r:
        return A[p]

    q = randomized_partition(A,p,r)
    k = q - p + 1

    if i == k: #pivot verdien er svaret
        return A[q]
    elif i < k:
        return randomized_select(A,p,q-1,i)
    else:
        return randomized_select(A,q+1,r,i-k)

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def randomized_partition(A,p,r):
    i = randint(p,r)
    A[r],A[i] = A[i],A[r]
    return partition(A,p,r)

start = time()
A = [randint(0,1000) for _ in range(1000)]
print(A)
print(randomized_select(A,0,len(A)-1,2))
end = time()
print(end-start)
