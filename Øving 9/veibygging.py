from sys import stdin

Inf = float(1e3000)

def mst(nm):
    min_spenntre = prims_algoritme(nm)
    return max(min_spenntre)

def prims_algoritme(nm):
    antall_noder = len(nm)
    key = [Inf]*antall_noder #Utvikler seg til å bli vektene til kantene i det minimale spenntreet
    parent = [None]*antall_noder
    key[0] = 0
    queue = [node_nr for node_nr in range(antall_noder)]
    while queue!=[]:
        current_node = queue.pop(0)
        for child in range(len(nm[current_node])):
            if child in queue and nm[current_node][child] < key[child]:
                parent[child] = current_node
                key[child] = nm[current_node][child]
    return key



lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
neighbour_matrix = [None] * n
node = 0
for line in lines:
    neighbour_matrix[node] = [Inf] * n
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node][neighbour] = weight
    node += 1
print (mst(neighbour_matrix))