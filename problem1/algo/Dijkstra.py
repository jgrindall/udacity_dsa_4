from .AAlgorithm import AAlgorithm
from .ShortestPath import ShortestPath

class Dijkstra(AAlgorithm):
    
    def __init__(self, graph):
        super().__init__(graph)


    def shortest_path(self, start, goal):
        if start == goal:
            return ShortestPath(0.0, [start])

        cities = list(self.graph.cities.keys())
        unvisited = cities
        shortest_path = {}
        previous_nodes = {}
        for node in unvisited:
            shortest_path[node] = float('inf')
        
        shortest_path[start] = 0

        def get_next_city():
            """ find the next node to visit """
            min_city = unvisited[0]
            min_value = shortest_path[min_city]
            for city in unvisited[1:]:
                d = shortest_path[city]
                if d < min_value:
                    min_city = city
                    min_value = d
            return min_city

        while len(unvisited) >= 1:
            city = get_next_city()
            unvisited.remove(city)
            neighbours = self.graph.get_neighbours(city)
            for neighbour in neighbours:
                if neighbour in unvisited:
                    val = shortest_path[city] + self.graph.get_road_length(city, neighbour)
                    if val < shortest_path[neighbour]:
                        shortest_path[neighbour] = val
                        # We also update the best path to the current node
                        previous_nodes[neighbour] = city

        #success
        if goal in previous_nodes:
            return ShortestPath(float(shortest_path[goal]), AAlgorithm.walk_backwards(start, goal, previous_nodes))
        
        #failure
        return ShortestPath()
