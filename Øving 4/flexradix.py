#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

BASE = 26

def flexradix(A, d):
    B = [0]*len(A)
    for i in range(d,0,-1):
        A = counting_sort(A,B,BASE,i-1)

    return B

def counting_sort(A,B,maxverdi,index):
    C = [0]*BASE
    for word in A:
        if len(word) - 1   == index:
            C[ord(word[index]) - ord('a')] += 1

    for i in range(1,maxverdi):
        C[i] += C[i-1]

    for j in range(len(A)-1,-1,-1):
        if len(A[j]) - 1  == index:
            B[C[ord(A[j][index]) - ord('a')] - 1] = A[j]
            C[ord(A[j][index]) -  ord('a')] -= 1

    ## Må finne ut hva jeg skal gjøre med de ordene som ikke har len -1 lik index..
    for i in range(0,len(B)):
        if B[i] == 0:
            p = 0
            element = A[0]
            check = True
            while element in B:
                p+=1
                element = A[p]
            B[i] = A[p]


    return B


def main():
    # d = int(stdin.readline())
    # strings = []
    # for line in stdin:
    #     strings.append(line.rstrip())
    # A = flexradix(strings, d)
    # for string in A:
    #     print(string)

    d = 9
    liste = ["tiger", "lion", "elephant", "zebra", "horse", "camel", "deer", "crocodile", "rabbit", "cat"]
    # d = 6
    # liste = ['kobra', 'alge', 'agg', 'kort', 'hyblen']
    print(flexradix(liste,d))



if __name__ == "__main__":
    main()

