class Node(object):
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def getValue(self):
        return self.data

    def __str__(self):
        return str(self.data)

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def __iter__(self):
        return iterate(self.head)

    def peek(self):
        return self.head.getValue()

    def isEmpty(self):
        return self.head == None

    # singly linked list #
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # for inserting at beginning of linked list
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    # for inserting at end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        if temp == None:
            self.head = newNode
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp

    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # for inserting at beginning of linked list
    def removeAtStart(self):
        temp = None
        if self.head == None:
            pass
        elif self.head.next == None:
            temp = self.head.data
            self.head = None
        else:
            temp = self.head.data
            self.head.next.previous = None
            self.head = self.head.next

    # deleting a node from linked list
    def delete(self, data):
        temp = self.head
        if temp == None:
            pass
        elif temp.next != None:
            # if head node is to be deleted
            if temp.data == data:
                temp.next.prev = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while temp.next != None:
                    if temp.data == data:
                        break
                    temp = temp.next
                if temp.next:
                    # if element to be deleted is in between
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = None
                    temp.prev = None
                else:
                    # if element to be deleted is the last element
                    temp.prev.next = None
                    temp.prev = None
                return
        if temp.next == None:
            pass

    # for printing the contents of linked lists
    def printdll(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next

    def findNode(self, data):
        # finds node containing a certain data
        temp = self.head
        while (temp.data != data):
            temp = temp.next
        return temp

# no need class #
class iterate():
    def __init__(self, head):
        self.cur = head

    def __next__(self):
        if self.cur == None:
            raise StopIteration
        else:
            data = self.cur.data
            self.cur = self.cur.next
            return data

