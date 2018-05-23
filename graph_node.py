class Node:
    def __init__(self, nodeId):
        self.id = nodeId
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def get_neighbours(self):
        return self.neighbours
