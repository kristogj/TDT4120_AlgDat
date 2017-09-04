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

    def multipop(self,k):
        while not self.isEmpty() and k > 0:
            self.pop()
            k -= 1

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def main():
    stack = Stack([1,2,3,4])
    print(stack)
    stack.multipop(3)
    print(stack)


main()