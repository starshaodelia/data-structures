class Queue:

    def __init__(self, length = 50):
        self.length = length
        self.queue = [None] * self.length
        self.front = self.rear = -1
        self.count = -1

    def getCount(self):
         return self.count + 1
        
    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return self.rear == self.length -1

    def enqueue(self, value):
        if self.isFull():
            raise Exception("The queue is full now.")
        if self.front == -1:
            self.front += 1
            self.rear += 1
        else:
            self.rear +=1
        self.count += 1
        self.queue[self.rear] = value
        return value

    def dequeue(self):
        if self.isEmpty():
            raise Exception("The queue is empty now.")
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        self.count -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise Exception('The stack is empty now')
        else:
            peekVal = self.queue[self.rear]
        return peekVal


    

    
