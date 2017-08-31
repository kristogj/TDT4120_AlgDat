#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge_sort(decks):
    result = make_one_list(decks)
    result_str = ""
    for tup in result:
        result_str += tup[1]
    return result_str

#Gjør decks om til en liste med tupler
def make_one_list(list):
    result = []
    for liste in list:
        for element in liste:
            result.append(element)
    return split(result)



#Splitter listen rekursivt
def split(list):
    if(len(list) <= 1):
        return list
    mid = int (len(list)//2)
    left = split(list[:mid])
    right = split(list[mid:])
    return merge(left,right)

#Sammenligner halvdeler, og limer sammen listene
def merge(left,right):
    result = []
    i,j = 0,0
    while(i<len(left) and j < len(right)):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result



def main():
    #Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
     #Merge the decks and print result.
    print(merge_sort(decks))



if __name__ == "__main__":
    main()