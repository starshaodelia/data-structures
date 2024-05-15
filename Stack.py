class Stack:

    def __init__(self, capacity = 10 ):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.count = -1

    def getCount(self):
        return self.count + 1

    def isEmpty(self):
        return self.count == -1

    def isFull(self):
        return self.count == self.capacity -1

    def push(self, value):
        if self.isFull():
            raise Exception('The stack is full now')
        else:
            self.count +=1
            self.stack[self.count] = value

    def pop(self):
        if self.isEmpty():
            raise Exception('The stack is empty now')
        else:
            topVal = self.top()
            self.count -= 1
        return topVal
        
    def top(self):
        if self.isEmpty():
            raise Exception('The stack is empty now')
        else:
            topVal = self.stack[self.count]
        return topVal

    def display(self):
        print(self.stack[:self.count+1])
