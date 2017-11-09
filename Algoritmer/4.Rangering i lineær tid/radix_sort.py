from time import time


#A = liste
#d = antall nummere i hvert element i hvor nummer 1 er nummeret med lavest grad
def raddix_sort(A,d):
    for i in range(d-1,-1,-1):
        A = counting_sort(A,9,i)
    return A

def counting_sort(A,max_verdi,d):
    result = [0]*len(A)
    counter = [0]*(max_verdi+1)

    for j in range(0,len(A)):
        element = int(str(A[j])[d]) #vi må se på det digit som skal telles
        counter[element] += 1

    for i in range(1,max_verdi+1):
        counter[i] += counter[i-1]

    for j in range(len(A)-1,-1,-1):
        element = A[j] #Hele elementet
        forekomster = counter[int(str(A[j])[d])]-1 #Forekomster av den digiten
        result[forekomster] = element #Legger hele elementet til i res
        counter[int(str(A[j])[d])] -= 1 #Trekker fra i counteren for den digiten
    return result



start = time()
A = [923, 134, 845, 274, 723, 345, 655, 467, 587, 900]
print(raddix_sort(A,len(str(A[0]))))
end = time()
print(end - start)