from time import time

#A = liste
#p = laveste index
#r = høyeste index

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    return A

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

start = time()
A = [9,1,8,2,7,3,6,4,5,0]
print(quicksort(A,0,len(A)-1))
end = time()
print(end-start)