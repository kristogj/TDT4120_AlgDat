#!/usr/bin/python3

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []



def bygg(ordliste):
    #Input: [('ha', 0), ('ha', 3), ('mons', 6), ('har', 11).....]
    rot = Node()
    for (word,pos) in ordliste:
        node = rot
        for ch in word:
            if ch not in node.barn:
                node.barn[ch] = Node()
                node = node.barn[ch]
            else:
                node = node.barn[ch]
        node.posi.append(pos)
    return rot


def posisjoner(ord, indeks, node):
    ch = ord[indeks]
    lengde = len(ord)-1
    if ch in node.barn:
        if indeks == lengde:
            return node.barn[ch].posi
        return posisjoner(ord,indeks+1,node.barn[ch])

    elif ch == '?':
        liste = []
        for k in node.barn.values():
            if indeks == lengde:
                liste += k.posi
            else:
                liste += posisjoner(ord,indeks+1,k)
        return liste
    else:
        return []


def main():
    from sys import stdin
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append((o, pos))
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print("%s:" % sokeord, end='')
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print(" %s" % p, end='')
        print()

if __name__ == "__main__":
    main()


