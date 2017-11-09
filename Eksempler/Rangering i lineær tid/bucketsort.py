import itertools

def bucket_sort(A):
    n = len(A)
    B = [[]]*n
    for i in range(0,n):
        B[int(n*A[i])] = B[int(n*A[i])] + [A[i]]
    for i in range(0,n-1):
        insertion_sort(B[i])
    return list(itertools.chain.from_iterable(B))

def insertion_sort(A):
    if A == []:
        return A
    i = 1
    # Sørger for at man itererer gjennom hele listen
    while i < len(A):
        j = i
        # Sålenge forje element er større enn det neste, og j ikke blir 0
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]  # swap
            j = j - 1
        i = i + 1
    return A

def main():

    liste = [0.53,0.54,0.39,0.42,0.38,0.83,0.96,0.12]
    print(bucket_sort(liste))

main()