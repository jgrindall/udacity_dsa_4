from abc import ABC, abstractmethod

class AAlgorithm(ABC):
    
    def __init__(self, graph):
        """ constructor. Store a refernce to the graph, of type AGraph"""
        self.graph = graph
        
    @staticmethod
    def walk_backwards(start, goal, previous_nodes):
        """ Eg.
            start = 0, goal = 10, previous nodes = {10: 8, 8:4, 4:0}
            This will return [0, 4, 8, 10]
            """
        path = [goal]
        city = goal
        while city != start:
            path.append(previous_nodes[city])
            city = previous_nodes[city]
        return list(reversed(path))

    @abstractmethod
    def shortest_path(self, start, goal):
        """subclasses should implement this """
        pass