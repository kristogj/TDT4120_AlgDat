#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    return



def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))
    print(decks)


if __name__ == "__main__":
    main()