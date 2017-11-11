from time import time

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
A = [9,1,8,2,7,3,6,4,5,0]*2000
print(insertion_sort(A))
end = time()
print(end-start)