from sys import stdin, stderr

stdin = open("input01.txt")

# Capacities is the original capacity-matrix, which contains n x n elemensts (where n is the amount of nodes)
# start_room is an array with the indexes to the nodes which corresponds to the start rooms.
# Exits is an array with the indexes to the nodes which corresponds to the exits.

def isolated_paths_count(capacities, start_rooms, exits):
    # You can use the method find_flow_path to simplify the problem
    # SKRIV DIN KODE HER
    print(capacities)
    print(start_rooms)
    print(exits)

# Finds a path from the source_node to the drain_node
# with available capacity in a flow-network with flow F and capacity C.
# Returns an array where the first element is the index to omne of the start nodes,
# last element is the index to one of the exits and the elements between
# are the indexes of the nodes along the path, in the correct order.
# Example: A path from the start node 4 to node 3, node 9, node 7 and finally
# to the exit 12 will be represented as [4,3,9,7,12].


def find_flow_path(source, drain, F, C):
    n = len(F)
    discovered = [False] * n
    parent = [None] * len(F)
    queue = [source]
    while queue:
        node = queue.pop(0)
        if node == drain:
            # The drain is found, create an array of passed nodes.
            path = []
            i = node
            while True:
                path.append(i)
                if i == source:
                    break
                i = parent[i]
            path.reverse()
            return path;
        for neighbour in range(n):
            if not discovered[neighbour] and F[node][neighbour] < C[node][neighbour]:
                queue.append(neighbour);
                discovered[neighbour] = True;
                parent[neighbour] = node;
    return None

antall_noder, antall_startnoder, antall_sluttnoder = [int(x) for x in stdin.readline().split()]
start_rooms = [int(x) for x in stdin.readline().split()]
exits = [int(x) for x in stdin.readline().split()]
adjacency_matrix = []
for linje in stdin:
    naborad = [int(nabo) for nabo in linje.split()]
    adjacency_matrix.append(naborad)
print(isolated_paths_count(adjacency_matrix, start_rooms, exits))