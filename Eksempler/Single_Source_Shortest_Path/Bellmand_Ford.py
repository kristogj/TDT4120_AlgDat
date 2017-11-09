
#nm [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
    #prob [1.0, 0.9, 0.3, 0.1, 0.8, 1.0]
class Node:

    def __init__(self,id):
        self.id = str(id)
        self.value = 0
        self.naboer = []
        self.visited = False

    def __repr__(self):
        return self.id

def best_path(nm,prob):
    graph = make_graph(nm,prob)
    s = []
    queue = [node for node in graph]
    possible = []
    while queue != []:
        u = queue.pop(0)
        possible = [node for node in u.naboer]
        liste = [node for node in possible]
        liste = sorted(liste,key=lambda x:x.value)
        best = liste[0]
        if best.visited:
            for node in liste:
                if not node.visited:
                    best = node
                    break
        best.visited = True
        s.append(best)
    return s


def extract_max(Q):
    #biggest first
    liste = sorted(Q,key= lambda node:node.value)
    Q.remove(liste[0])
    return liste[0]

def make_graph(nm,prob):
    nodes = len(prob)
    graph = [Node(x) for x in range(nodes)]
    for node in range(nodes):
        graph[node].value = prob[node]
        naboer = []
        for nabo in range(len(nm[node])):
            if nm[node][nabo] == 1:
                naboer.append(graph[nabo])
        graph[node].naboer = naboer
    return graph




def main():
    nm = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
    prob = [1.0, 0.9, 0.3, 0.1, 0.8, 1.0]
    graph = best_path(nm,prob)

    print(graph)

    # n1 = Node(0)
    # n2 = Node(1)
    # n3 = Node(2)
    #
    # n1.value = 1
    # n2.value = 3
    # n3.value = 0
    #
    # liste = [n1,n2,n3]
    # extract_max(liste)

main()
