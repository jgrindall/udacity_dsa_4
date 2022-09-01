import math

class AGraph:
    
    def __init__(self, cities, roads, road_lengths = None, heuristics = None):
        """ Store cities, roads. Calculate road_lengths and heuristics if they are not given """
        self.cities = cities
        self.roads = roads
        
        self.road_lengths = road_lengths
        if self.road_lengths is None:
            self.road_lengths = {}
            self.__build_road_lengths()
        
        self.heuristics = heuristics
        if self.heuristics is None:
            self.heuristics = {}
            self.__build_heuristics()
    
    def get_neighbours(self, city):
        """ all cities adjacent to 'city' """
        return self.roads[city]

    def get_road_length(self, city0, city1):
        """ length of road from 0 to 1 """
        return self.road_lengths[city0][city1]
    
    def get_heuristic_length(self, city0, city1):
        if city0 not in self.heuristics:
            print(self.heuristics)
            raise ValueError("h")
        return self.heuristics[city0][city1]

    def __build_road_lengths(self):
        """if road lengths are not specified, assume straight-line Euclidean"""
        for city in self.cities:
            self.road_lengths[city] = {}
            neighbours = self.get_neighbours(city)
            for neighbour in neighbours:
                p0 = self.cities[city]
                p1 = self.cities[neighbour]
                self.road_lengths[city][neighbour] = AGraph.get_euclidean_dist(p0, p1)
    
    def __build_heuristics(self):
        """ build an array of heuristic lengths between every city
            self.heur[a][b] = heuristic (straight line distance) between a and b
        """
        def build(city0):
            self.heuristics[city0] = {}
            for city1 in self.cities:
                self.heuristics[city0][city1] = AGraph.get_euclidean_dist(self.cities[city0], self.cities[city1])
        for city in self.cities:
            build(city)

    @staticmethod
    def get_euclidean_dist(p0, p1):
        """Helper function """
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        return math.sqrt(dx*dx + dy*dy)
