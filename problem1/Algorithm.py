import math
from abc import ABC, abstractmethod

class Algorithm(ABC):
    
    def __init__(self, cities, roads, road_lengths = None):
        """ doc"""
        self.cities = cities
        self.roads = roads
        self.road_lengths = road_lengths
        if self.road_lengths is None:
            self.build_road_lengths()
    
    def get_road_length(self, city0, city1):
        return self.road_lengths[city0][city1]
    
    def build_road_lengths(self):
        """if road lengths are not specified, assume straight-line Euclidean"""
        self.road_lengths = {}
        for city in self.cities:
            self.road_lengths[city] = {}
            neighbours = self.get_neighbours(city)
            for neighbour in neighbours:
                p0 = self.cities[city]
                p1 = self.cities[neighbour]
                self.road_lengths[city][neighbour] = Algorithm.get_euclidean_dist(p0, p1)
    
    @staticmethod
    def walk_backwards(start, goal, previous_nodes):
        path = [goal]
        city = goal
        while city != start:
            path.append(previous_nodes[city])
            city = previous_nodes[city]
        return path
    
    @staticmethod
    def get_euclidean_dist(p0, p1):
        """Helper function """
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        return math.sqrt(dx*dx + dy*dy)
    
    def get_neighbours(self, city):
        return self.roads[city]
    
    @abstractmethod
    def shortest_path(self, start):
        pass