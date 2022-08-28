from Node import Node
from MinHeap import MinHeap
from Algorithm import Algorithm

class AStar(Algorithm):
    def __init__(self, cities, roads, road_lengths = None, heuristics = None):
        super().__init__(cities, roads, road_lengths)
        self.heuristics = heuristics
        if self.heuristics is None:
            self.build_heuristics()

    def build_heuristics(self):
        """ build an array of heuristic lengths between every city
            self.heur[a][b] = heuristic (straight line distance) between a and b
        """
        self.heuristics = {}
        def build(city0):
            self.heuristics[city0] = {}
            for city1 in self.cities:
                p0 = self.cities[city0]
                p1 = self.cities[city1]
                self.heuristics[city0][city1] = Algorithm.get_euclidean_dist(p0, p1)
        for city in self.cities:
            build(city)

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
            city_node = frontier.remove()
            city = city_node.city
            visited[city] = True
            if city_node.city == goal:
                # We found it
                return {
                    "path": Algorithm.walk_backwards(start, goal, previous_nodes),
                    "length": city_node.f_value
                }

            
            else:
                neighbours = self.get_neighbours(city_node.city)
                for neighbour in neighbours:
                    
                    if neighbour in visited:
                        continue
                    
                    g_value = city_node.g_value + self.get_road_length(city_node.city, neighbour)
                    h_value = self.get_heuristic_length(neighbour, goal)
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

