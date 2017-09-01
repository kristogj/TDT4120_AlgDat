#Insertionsort

def sort(A):
    i = 1
    #Sørger for at man itererer gjennom hele listen
    while i < len(A):
        j = i
        #Sålenge forje element er større enn det neste, og j ikke blir 0
        while j > 0 and A[j-1] > A[j]:
            A[j],A[j-1] = A[j-1],A[j] #swap
            j = j-1
        i = i + 1
    return A

def main():
    liste = [8,9,7,6,5,4,3,2,1]
    print(sort(liste))

main()