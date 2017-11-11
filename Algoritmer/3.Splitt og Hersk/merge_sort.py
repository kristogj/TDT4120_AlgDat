from time import time

#A = liste
def merge_sort(A):
    if len(A) > 1:
        q = len(A)//2

        #Del A i Left og Right
        L = merge_sort(A[:q])
        R = merge_sort(A[q:])

        return merge(L,R)
    return A #Grunntilfellet len(A) = 1 er en sortert liste

def merge(L,R):
    res = []

    i = 0
    j = 0
    while i<len(L) and j<len(R):
        if L[i] < R[j]: #Hvis Left element er mindre en Right, må den legges til først
            res.append(L[i])
            i+=1
        else:
            res.append(R[j])
            j+=1
    #De resterende elementene er allerede sortert da. Mangler enten fra L eller fra R. Aldri begge
    if i < len(L): res+=L[i:]
    if j < len(R): res+=R[j:]

    return res


start = time()
A = [9,1,8,2,7,3,6,4,5,0]*10000
print(merge_sort(A))
end = time()
print(end-start)

#Til sammenligning:
#Insertion-sort brukte: 6.352623701095581 sek på 10 000 elementer
#Merge-sort brukte: 0.08375787734985352 sek på 10 000 elementer