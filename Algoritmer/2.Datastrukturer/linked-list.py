
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None

    def __repr__(self):
        return "Node: " + str(self.key)

class Linked_List():

    def __init__(self):
        self.head = None

    def search(self,k):
        node = self.head
        while node != None and node.key != k:
            node = node.next
        return node

    def insert(self,node):
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node
        node.prev = None

    def delete(self,node):
        if node.prev != None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next != None:
            node.next.prev = node.prev

    def __str__(self):
        res = []
        x = self.head
        while x != None:
            res.append(x)
            x = x.next
        return str(res)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

L = Linked_List()
L.insert(n1)
L.insert(n2)
L.insert(n3)
L.insert(n4)
print(L)
print(L.search(1))
L.delete(n3)
print(L)

