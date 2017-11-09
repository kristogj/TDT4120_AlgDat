#!/usr/bin/python3

from sys import stdin


class Seddel:
    def __init__(self,width,height,verdi):
        self.width = width
        self.height = height
        self.verdi = verdi

    def __eq__(self, other):
        return (self.height == other.height and self.width == other.width) or (self.height == other.width and self.width == other.height)

    def __gt__(self, other):
        return (self.height > other.height and self.width > other.width) or (self.height > other.width and self.width > other.height)

#input først([2, 2, 4], [3, 3, 5], [5, 4, 16], 10, 3) --> out 25. som er 5 5ére
#      secon([2, 2, 4], [3, 3, 5], [5, 4, 16], 7, 4) --> out 21. som er en av hver seddel
def max_value(widths, heights, values, paperWidth, paperHeight):
    kapasitet = max(paperHeight,paperWidth)
    antall_elementer = len(values)
    K = [[0 for x in range(kapasitet+1)] for x in range(antall_elementer+1)]

    for i in range(antall_elementer + 1):
        for w in range(kapasitet + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif min(widths[i-1], heights[i-1]) <= w:
                K[i][w]= max(values[i-1] + K[i-1][w-(min(widths[i-1],heights[i-1]))],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
        print(K)
        return K[antall_elementer][kapasitet]




def knapSack(kapasitet, vekter, verdier, antall_elementer):
    K = [[0 for x in range(kapasitet + 1)] for x in range(antall_elementer + 1)]

    for i in range(antall_elementer + 1):
        for w in range(kapasitet + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif vekter[i - 1] <= w:
                K[i][w] = max(verdier[i - 1] + K[i - 1][w - vekter[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[antall_elementer][kapasitet]


def main():
    # widths = []
    # heights = []
    # values = []
    # for triple in stdin.readline().split():
    #     dim_value = triple.split(':', 1)
    #     dim = dim_value[0].split('x', 1)
    #     width = int(dim[0][1:])
    #     height = int(dim[1][:-1])
    #     value = int(dim_value[1])
    #     widths.append(int(width))
    #     heights.append(int(height))
    #     values.append(int(value))
    # for line in stdin:
    #     paper_width, paper_height = [int(x) for x in line.split('x', 1)]
    #     print((max_value(widths, heights, values, paper_width, paper_height)))

    widths = [2,2,4]
    heights = [3,3,5]
    values = [5,4,16]
    paper_width = 10
    paper_height = 3
    print(max_value(widths,heights,values,paper_width,paper_height))
    print()
    widths = [2, 2, 4]
    heights = [3, 3, 5]
    values = [5, 4, 16]
    paper_width = 7
    paper_height = 4
    print(max_value(widths, heights, values, paper_width, paper_height))

main()
# if __name__ == "__main__":
#      main()