#!/usr/bin/python3
from sys import stdin



class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
        self.depth = 0


def dfs(root):
    stack = []
    stack.append(root)
    while stack!= []:
        u = stack.pop()
        if u.ratatosk:
            return u.depth
        for child in u.child:
            child.depth = u.depth + 1
        stack += u.child

def bfs(root):
    queue = [root]
    while queue != []:
        u = queue.pop(0)
        if u.ratatosk:
            return u.depth
        for node in u.child:
            queue.append(node)
            node.depth = u.depth + 1



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
    print(dfs(start_node))
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
    print(dfs(start_node))