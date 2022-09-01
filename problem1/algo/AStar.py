from .Node import Node
from .AAlgorithm import AAlgorithm
from .ShortestPath import ShortestPath
import heapq

class PriorityQueue:
    """ See https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes """
    def __init__(self):
        # this is the heap
        self.list = []
        
        # map city to item in the heap for convenience
        self.lookup = {}
        
        #store the size (non-removed)
        self.size = 0
    
    def get_lookup(self, city):
        return self.lookup[city] if city in self.lookup else None
    
    def get_size(self):
        return self.size
    
    def add(self, node):
        heapq.heappush(self.list, node)
        self.lookup[node.city] = node
        self.size += 1
        
    def pop(self):
        #keep popping the removed ones, they are red-herrings
        while len(self.list) >= 1:
            node = heapq.heappop(self.list)
            if not node.removed:
                self.size -= 1
                return node
    
    def update(self, node, g_value):
        new_node = Node(node.city, g_value, node.h_value)
        old_node = self.lookup[node.city]
        old_node.removed = True
        heapq.heappush(self.list, new_node)
        self.lookup[node.city] = new_node


class AStar(AAlgorithm):
    def __init__(self, graph):
        super().__init__(graph)

    def get_heuristic_length(self, city0, city1):
        return self.heuristics[city0][city1]

    def shortest_path(self, start, goal):
        if start == goal:
            #short-circuit return
            return ShortestPath(0.0, [start])

        """Run the A* algorithm"""


        # The format of each item in the heap is: Node(city, g, h)
        # The heap will sort using the __lt__ and __gt__ functions implemented in the Node class.
        start_node = Node(start, 0, self.graph.get_heuristic_length(start, goal))
        
        #make the heap
        frontier = PriorityQueue()
        frontier.add(start_node)
        
        # store where we have been
        visited = {}
        
        # and the previous node from each city so we can back-track to construct the full path
        previous_nodes = {}

        while frontier.get_size() >= 1:
            # get the minimum f-value
            node = frontier.pop()
            city = node.city
            visited[city] = True
            if city == goal:
                # We found it
                return ShortestPath(float(node.f_value), AAlgorithm.walk_backwards(start, goal, previous_nodes))
            else:
                neighbours = self.graph.get_neighbours(city)
                for neighbour in neighbours:
                    if neighbour in visited:
                        continue
                    
                    # get the new g_value and h_value
                    g_value = node.g_value + self.graph.get_road_length(city, neighbour)
                    h_value = self.graph.get_heuristic_length(neighbour, goal)
                    # see if we have already been to this node
                    existing_node = frontier.get_lookup(neighbour)

                    if existing_node is None:
                        #insert it
                        new_node = Node(neighbour, g_value, h_value)
                        frontier.add(new_node)

                    elif g_value < existing_node.g_value:
                        #better
                        frontier.update(existing_node, g_value)

                    #also create the path back
                    previous_nodes[neighbour] = city

        # failure condition
        return ShortestPath()

