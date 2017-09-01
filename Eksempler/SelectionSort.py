#SelectionSort
#Velg det laveste eleementet og swap det inn i første posisjonen, finn så det nest laveste ved å scanne n-1 elementer,
#swap det inn i nest laveste posisjon osv osv..
def sort(a):
    i,j = 0,0
    n = len(a)

    for j in range(0,n-1):
        iMin = j
        for i in range(j+1,n):
            if a[i] < a[iMin]:
                iMin = i

        if iMin != j:
            a[j],a[iMin] = a[iMin],a[j]

    return a

def main():
    liste = [9,8,7,6,5,4,3,2,1]
    print(sort(liste))

main()