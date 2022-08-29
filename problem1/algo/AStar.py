from .Node import Node
from .MinHeap import MinHeap
from .AAlgorithm import AAlgorithm

class AStar(AAlgorithm):
    def __init__(self, graph):
        super().__init__(graph)

    def get_heuristic_length(self, city0, city1):
        return self.heuristics[city0][city1]

    def shortest_path(self, start, goal):
        """Run the A* algorithm"""
        frontier = MinHeap()
        frontier.insert(Node(start, 0, 0))
        visited = {}
        previous_nodes = {}
        
        #print("frontier", frontier)
        
        while not frontier.get_is_empty():
            node = frontier.remove()
            city = node.city
            visited[city] = True
            if city == goal:
                # We found it
                return {
                    "length": node.f_value,
                    "path": AAlgorithm.walk_backwards(start, goal, previous_nodes)
                }
            else:
                neighbours = self.graph.get_neighbours(city)
                for neighbour in neighbours:
                    
                    if neighbour in visited:
                        continue
                    
                    g_value = node.g_value + self.graph.get_road_length(city, neighbour)
                    h_value = self.graph.get_heuristic_length(neighbour, goal)
                    existing_node =  frontier.get_by_key(neighbour)
                    
                    if existing_node is None:
                        frontier.insert(Node(neighbour, g_value, h_value))
                        previous_nodes[neighbour] = city
                    else:
                        if existing_node.g_value > g_value:
                            #better
                            existing_node.g_value = g_value
                            previous_nodes[neighbour] = city
                            #f value has changed - re-heapfiy the heap
                            frontier.heapify()
        return None

