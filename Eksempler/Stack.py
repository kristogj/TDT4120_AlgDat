#Stack

class Stack():

    def __init__(self,lst):
        self.items = lst


    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.lst[0:self.top + 1]) + " top_index = " + str(self.top)

def main():
    stack = Stack([1,2,3,4])


main()