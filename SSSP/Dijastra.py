# Dijastra works for weighted and unweighted graph to find shortest path.
# But it won't work for negative cycles.


class Edge:
    def __init__(self, weight, start_vertex, traget_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.traget_vertex = traget_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        # previous node form which we come to this edge
        self.predessor = None
        self.neighbours = []
        self.min_distance = float("inf")

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
