from time import time

def counting_sort(A,max_verdi):
    result = [0]*len(A) #Output listen, må ha samme lengde som
    counter = [0]*(max_verdi+1) #Må ha +1 pga 0 kan også være en verdi


    for j in range(0,len(A)):
        counter[A[j]] += 1

    #C[i] inneholder nå antall forekomster av element i
    #Så C[0] er antall forekomster av 0, C[1] forekomster av 1 osv..

    for i in range(1,max_verdi+1):
        counter[i] += counter[i-1]
    #C[i] inneholder nå antall elementer mindre eller lik i
    #Så C[0] vil bare inneholde antall forekomster av seg selv, men C[1] vil inneholder forekomster av seg selv + forekomster av 0

    #Må iterere baklengs for at coutning sort skal være stabil
    for j in range(len(A)-1,-1,-1):
        element = A[j] #Elementet vi ser på nå
        forekomster = counter[element]-1 #Må trekke fra 1 pga 0 er også med
        result[forekomster] = A[j]
        counter[element] -= 1 #elementet er lagt til i resultat, trekk fra 1 i counteren
    return result



start = time()
A = [9, 1, 8, 2, 7, 3, 6, 4, 5, 9]
print(counting_sort(A,max(A)))
end = time()
print(end - start)