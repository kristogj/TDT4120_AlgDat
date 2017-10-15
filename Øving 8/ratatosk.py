#!/usr/bin/python3

from sys import stdin



class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
        self.depth = 0


def dfs(root):
    if root.ratatosk:
        return root.depth
    for child in root.child:
        child.depth += 1
        dfs_visit(child)

def dfs_visit(node):
    for child in node.child:

        dfs_visit(child)


def bfs(root):
    #head index 0
    queue = [root]
    depth = 0
    while queue != []:
        u = queue.pop(0)
        if u.ratatosk:
            return u.depth
        for node in u.child:
            queue.append(node)
            node.depth = u.depth + 1
    return None



function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])

if function == 'dfs':
    print(bfs(start_node)) #Endre denne...
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
    print(bfs(start_node))