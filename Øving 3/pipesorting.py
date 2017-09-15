#!/usr/bin/python3

from sys import stdin


def sort_list(A):
    # NOTICE: The sorted list must be returned.
    # SKRIV DIN KODE HER
    return split(A)

def split(A):
    if (len(A) < 2):
        return A
    left = split(A[:len(A) // 2])
    right = split(A[len(A) // 2:])
    return merge(left, right)

def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result



def find(A, nedre, ovre):
    indeks_nedre = binsok(A, nedre)
    indeks_ovre = binsok(A, ovre)
    if A[indeks_nedre] > nedre and indeks_nedre != 0:
        indeks_nedre -= 1
    if A[indeks_ovre] < ovre and indeks_ovre != len(A) - 1:
        indeks_ovre += 1
    return [A[indeks_nedre], A[indeks_ovre]]

def binsok(A, verdi):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if verdi == A[m]:
            break
        elif verdi < A[m]:
            r = m - 1
        else:
            l = m + 1

    return m



def main():
    # input_list = []
    # for x in stdin.readline().split():
    #     input_list.append(int(x))
    #
    # sorted_list = sort_list(input_list)
    #
    # for line in stdin:
    #     word = line.split()
    #     minimum = int(word[0])
    #     maximum = int(word[1])
    #     result = find(sorted_list, minimum, maximum)
    #     print(str(result[0]) + " " + str(result[1]))

    in_list = [12, 90, 5, 18, 140, 130, 143, 70]
    sortert = sort_list(in_list)
    print(find(sortert,5,70))

main()
if __name__ == "__main__":
    main()