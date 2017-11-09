

class Stack:

    def __init__(self):
        self.stack = [None]*100
        self.top = -1

    def stack_is_empty(self):
        return self.top == -1

    def push(self,x):
        self.top += 1
        self.stack[stack.top] = x

    def pop(self):
        if self.stack_is_empty():
            return "error underflow"
        else:
            self.top -=1
            return self.stack[self.top+1]

    def __str__(self):
        return str(self.stack)


stack = Stack()
stack.push(5)
stack.push(6)
stack.push(3)
stack.push(2)
print(stack)
print(stack.pop())
stack.push(66)
print(stack)
print(stack.pop())


