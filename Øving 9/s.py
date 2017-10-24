# -*- coding: utf-8 -*-
from sys import stdin


class UF:
    """Implementation of weighted quick-union with path compression"""

    def __init__(self):
        """Initialize data structure"""
        self.id = {}  # Use a dictionary, to support all data types
        self.sz = {}  # Ditto. This contains the size of the tree at p
        self.count = 0

    def add(self, p):
        """Add site to data structure"""
        self.id[p] = p  # A root site points to itself
        self.sz[p] = 1  # Component with a single site has size 1
        self.count += 1

    def union(self, p, q):
        """Add connection between p and q"""
        i = self.find(p)
        j = self.find(q)
        if i == j: return

        # Make smaller root point to larger one
        # This is the weighted union
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

        self.count -= 1

    def find(self, p):
        """Return the root site of the component p belongs to"""
        # Copy the reference, so we don't change the input
        root = q = p

        # Find the root node
        while root != self.id[root]:
            root = self.id[root]

        # Find it again, this time changing the pointers to root.
        # This is the path compression
        while q != root:
            q_copy = self.id[q]
            self.id[q] = root
            q = q_copy

        return root

    def connected(self, p, q):
        """Return true if p and q are in the same component"""
        return self.find(p) == self.find(q)

    def __repr__(self):
        return str(self.id.keys()) + "\n" + str(self.id.values())


Inf = float(1e3000)
# False = 0
# True = 1


def mst(nm):
    kanter = []
    # Hold orden p책 komponenter i MST-et
    T = UF()
    for i in range(0, N):
        T.add(i)
        for j in range(0, i):
            # kant med lengde nm[i][j] fra i til j
            kanter.append((nm[i][j], i, j))

    # Sorter etter lengde p책 kanter
    # Omvendt, slik at pop() bruker konstant tid
    kanter.sort(reverse=True)

    antall_noder = 0
    dyreste = -Inf

    # S책 lenge ikke alle noder er med i treet
    while T.count != 1:
        # Hent en kant fra stakken
        kant = kanter.pop()
        # Sjekk om begge ligger i samme komponent som treet
        if not T.connected(kant[1], kant[2]):
            # Ny kant
            T.union(kant[1], kant[2])
            # Sjekk om det er den korteste
            dyreste = max(dyreste, kant[0])

    return dyreste


linjer = []
for str in stdin:
    linjer.append(str)
N = len(linjer)
nabomatrise = [None] * N
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * N
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1

print(mst(nabomatrise))