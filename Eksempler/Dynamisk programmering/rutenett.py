def T(m,n):
    if m==1 or n==1:
        return 1
    return T(m-1,n)+T(m,n-1)

def main():
    print(T(4,3))

main()