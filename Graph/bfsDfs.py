# Used for graph Traversal.
# It starts from some artibitary node of the graph and explaore neighbour node
# first before moving to next node.
# Why set()---> because performance of set to check if nodes are their already, set contains
# unique elements only.

from collections import deque


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

    # def bfs(self, vertex):
    #     visited = set()
    #     visited.add(vertex)
    #     queue = [vertex]
    #     while queue:
    #         current_vertex = queue.pop(0)
    #         print(current_vertex)
    #         for adjecent_vertex in self.adjecencyList[current_vertex]:
    #             if adjecent_vertex not in visited:
    #                 visited.add(adjecent_vertex)
    #                 queue.append(adjecent_vertex)

    # Generally time complexity for BFS is O(V+e), but due to queue.pop(0) tc goes to O(n) coz for pop in queue we have to shift elements one step back.
    # Hence, instead we will use deque for O(1) tc so that BFS is O(V+e)

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:  # ---> O(V)
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjecent_vertex in self.adjecencyList[current_vertex]:  # --->O(E)
                if adjecent_vertex not in visited:
                    visited.add(adjecent_vertex)
                    queue.append(adjecent_vertex)

    # It starts from some artibitary node of the graph and explore as far as possible
    # along each edge before backtracking.
    # Difference between DFS and BFS :-
    # In dfs we go as deep as possibleusing a given edge. Once, we reached the bottom we do backtracking
    # In bfs we used queue, here we will use Stack

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.adjecencyList[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)


customGraph = Graph()
customGraph.addVertex("A")
customGraph.addVertex("B")
customGraph.addVertex("C")
customGraph.addVertex("D")
customGraph.addVertex("E")
customGraph.addEdge("A", "B")
customGraph.addEdge("A", "C")
customGraph.addEdge("B", "E")
customGraph.addEdge("C", "D")
customGraph.addEdge("D", "E")
print("----- Graph -----")
customGraph.printGraph()
print("----- BFS -----")
customGraph.bfs("A")
print("----- DFS -----")
customGraph.dfs("A")
