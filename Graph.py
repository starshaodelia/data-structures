from LinkedList import *

class Edge:
    def __init__(self, n1, n2, weight):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighborList = DoublyLinkedList() # list of edges #
        self.visited = False

    def getLabel(self):
        return self.label

    def getAdj(self):
        adj = DoublyLinkedList()
        for edge in self.neighborList:
            adj.insertAtEnd(edge.n2)
        return adj

    def addEdge(self, edge):
        self.neighborList.insertAtEnd(edge)

    def __str__(self):
        return str(self.label) + " | " + " ".join([str(v.n2.label) for v in self.neighborList]) + "\n"

class Graph:
    def __init__(self):
        self.vertices = DoublyLinkedList()
        self.edgeList = DoublyLinkedList()
        # vertices are arranged as linkedlist #

    def hasvertex(self, label):
        for nd in self.vertices:
            if nd.label == label:
                return True
        return False

    def vertexCount(self):
        return self.vertices.count()

    def getvertex(self, label):
        for nd in self.vertices:
            if nd.label == label:
                return nd

    def addvertex(self, label):
        v = Vertex(label)
        if self.vertices.head is None:
            self.vertices.push(v)
        else:
            self.vertices.insertAtEnd(v)
        return v

    def addedge(self, label1, label2, weight):
        if self.hasvertex(label1) is False:
            one = self.addvertex(label1)
        else:
            one = self.getvertex(label1)
        if self.hasvertex(label2) is False:
            two = self.addvertex(label2)
        else:
            two = self.getvertex(label2)
        # undirected graph #
        edge1 = Edge(one, two, weight)
        edge2 = Edge(two, one, weight)
        # adds edges to edgeList
        self.edgeList.push(edge1)
        self.edgeList.push(edge2)
        one.addEdge(edge1)
        two.addEdge(edge2)

    def displaygraph(self):
        self.vertices.printdll()

    def breadthfirst(self, src):
        visited = DoublyLinkedList()
        visited.push(src)
        # q is a linkedlist that behaves like shuffle queue #
        q = DoublyLinkedList()
        q.insertAtStart(src)
        # insert source node in queue #
        while not q.isEmpty():
            v = q.peek()
            q.removeAtStart()
            for n in v.getAdj():
                if n not in visited:
                    q.insertAtEnd(n)
                    visited.insertAtEnd(n)
        return visited

    def depthfirst(self, visited, s):
        # recursive method
        while not s.isEmpty():
            # keep in mind: linkedlist behaves as stack
            v = s.peek()
            s.removeAtStart()
            for n in v.getAdj():
                if n not in visited:
                    s.insertAtStart(n)
                    visited.insertAtEnd(n)
                    self.depthfirst(visited, s)
        return visited

    def dfs(self):
        # wrapper for recursion
        visited = DoublyLinkedList()
        visited.insertAtEnd(self.vertices.peek())
        s = DoublyLinkedList()
        # inserting source node in queue
        s.insertAtStart(self.vertices.peek())
        return self.depthfirst(visited, s)

    def bfs(self):
        return self.breadthfirst(self.vertices.peek())

    def getWeight(self, label1, label2):
        n1 = self.getvertex(label1)
        n2 = self.getvertex(label2)
        for edge in n1.neighborList:
            if edge.n2 == n2:
                return edge.weight

