
class Queue:

    def __init__(self):
        self.queue = [None]*3
        self.head = 0
        self.tail = 0
        self.length = 0

    def enqueue(self,x):
        self.queue[self.tail] = x
        if self.tail == len(self.queue)-1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        x = self.queue[self.head]
        if self.head == len(self.queue)-1:
            self.head = 0
        else:
            self.head += 1
        return x

    def __str__(self):
        return str(self.queue) + "\n" + str(self.head) + "\n" + str(self.tail)
q = Queue()
q.enqueue(5)
print(q)
q.dequeue()
print(q)
q.enqueue(6)
print(q)
q.enqueue(7)
print(q)
q.dequeue()
print(q)
q.enqueue(77)
print(q)
print(q.dequeue())
print(q.dequeue())

