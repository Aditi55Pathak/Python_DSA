class Graph:
    def __init__(self):
        self.adjecencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjecencyList.keys():
            self.adjecencyList[vertex] = []
            return True
        return False

    def printGraph(self):
        for vertex in self.adjecencyList:
            print(vertex, ":", self.adjecencyList[vertex])

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjecencyList and vertex2 in self.adjecencyList:
            self.adjecencyList[vertex1].append(vertex2)
            self.adjecencyList[vertex2].append(vertex1)
            return True
        return False

    def RemoveEdge(self, vertex1, vertex2):
        if vertex1 in self.adjecencyList and vertex2 in self.adjecencyList:
            self.adjecencyList[vertex2].remove(vertex1)
            self.adjecencyList[vertex1].remove(vertex2)
            return True
        return False


customGraph = Graph()
customGraph.addVertex("A")
customGraph.addVertex("B")
customGraph.addVertex("C")
customGraph.addEdge("A", "B")
customGraph.addEdge("A", "C")
customGraph.addEdge("B", "C")
print("----- Graph -----")
customGraph.printGraph()
customGraph.RemoveEdge("A", "C")
print("----- Graph Removal -----")
customGraph.printGraph()
print("----- Graph Add -----")
customGraph.addVertex("D")
customGraph.addEdge("A","D")
customGraph.addEdge("D","C")
customGraph.printGraph()