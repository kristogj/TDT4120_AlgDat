def countingsort(A,k,index):
    #A Liste med bokstaver k maksverdi = 122 (ord(z)), min er a  = 97
    lovlig = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    B = [None]*(len(A)+1)
    C = [0]*len(lovlig) #index 97-122 altså a-z  len(C) = 26

    for j in range(0,len(A)):
        C[ord(A[j]) - 97] += 1
    print("C:" + str(C))

    for i in range(1,k):
        C[i] += C[i-1]
    print("C:" + str(C))

    for j in range(len(A)-1,-1,-1):

        B[C[ord(A[j]) - 97]] = A[j]
        C[ord(A[j])-97] -= 1

    B.pop(0)
    print(A)
    print(B)
    print(C)
    print()
    return(B)