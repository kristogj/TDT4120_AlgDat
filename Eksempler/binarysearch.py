

def binary_search(A,num):
    mid = A[len(A)//2]
    if num == mid:
        return True
    elif num > mid:
        binary_search(A[A.index(mid):],num)
    else:
        binary_search(A[:A.index(mid)],num)

def main():
    liste = [1,2,3,4,5,6,7,8,9]
    print(binary_search(liste,4))

main()