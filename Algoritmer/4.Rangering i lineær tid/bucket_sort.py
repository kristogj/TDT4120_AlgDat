from time import time
from random import uniform

def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(0,n):
        B[int(n*A[i])].append(A[i])
    for bucket in B:
        insertion_sort(bucket)
    return [value for bucket in B for value in bucket]

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]

        #Plasser A[j] inn i den sorterte sub-sekvensen [0...j-1]
        i = j-1
        while i >= 0 and A[i] > key:

            #Flytter hvert element til høyre sålenge key < A[i]
            A[i+1] = A[i]
            i = i-1

        #Plasser key på riktig plass
        A[i+1] = key
    return A

start = time()
A = [round(uniform(0,0.999),3) for _ in range(10)]
print(A)
print(bucket_sort(A))
end = time()
print(end-start)