from map1 import Map as map1
from map2 import Map as map2

import math 

class N():
    def __init__(self, cities, f):
        self.cities = cities
        self.f = f

    def __repr__(self):
        return "cities: " + str(self.cities) + " f: " + str(self.f)

    def __str__(self):
        return self.__repr__()
    

class AStar():
    def __init__(self, cities, roads, heur = None, road_lengths = None):
        self.cities = cities
        self.roads = roads
        self.road_lengths = road_lengths
        self.heur = heur
        if self.heur is None:
            self.build_heur()
        
        if self.road_lengths is None:
            self.build_road_lengths()
    
    def build_heur(self):
        """ build an array of heuristic lengths between every city
            self.heur[a][b] = straight line distance from a to b
        """
        self.heur = {}
        def build(city0):
            self.heur[city0] = {}
            for city1 in self.cities:
                self.heur[city0][city1] = self.get_heuristic_length(city0, city1)
        for city in self.cities:
            build(city)

    def build_road_lengths(self):
        """if road lengths are not specified, assume straight-line Euclidean"""
        self.road_lengths = {}
        for city in self.cities:
            self.road_lengths[city] = {}
            neighbours = self.get_neighbours(city)
            for neighbour in neighbours:
                p0 = self.cities[city]
                p1 = self.cities[neighbour]
                self.road_lengths[city][neighbour] = AStar.get_euclidean_dist(p0, p1)
    
    def get_heuristic_length(self, city0, city1):
        """ Use Euclidean """
        p0 = self.cities[city0]
        p1 = self.cities[city1]
        return AStar.get_euclidean_dist(p0, p1) 

    def get_neighbours(self, city):
        return self.roads[city]
    
    @staticmethod
    def get_euclidean_dist(p0, p1):
        """Helper function """
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        return math.sqrt(dx*dx + dy*dy)
    
    def get_road_length(self, city0, city1):
        """ Get the length of the road from city0 to city1 """
        return self.road_lengths[city0][city1]

    def shortest_path(self, start, goal):
        """Run the A* algorithm """
        frontier = {}
        frontier[start] = N([start], 0)
        
        
        def get_expand():
            min = float('inf')
            _city = None
            for city in frontier:
                if frontier[city].f < min:
                    min = frontier[city].f
                    _city = city
            return _city
        
        print("frontier", frontier)
        n = 0
        while True and n < 2:
            
            city = get_expand()
            
            print("city", city)
            
            if city == goal:
                break
            
            neighbours = self.get_neighbours(city)
            for neighbour in neighbours:
                
                print('neighbour', neighbour)
                
                print('f', frontier[city].f)
                print('add', self.get_road_length(city, neighbour))
                print('heur', self.get_heuristic_length(neighbour, goal))
                
                f = frontier[city].f + self.get_road_length(city, neighbour) + self.get_heuristic_length(neighbour, goal)
                new_path = frontier[city].cities + [neighbour]
                frontier[neighbour] = N(new_path, f)
        
            print("frontier", frontier)     
           
            n += 1
            
        return


a = AStar(map2.cities, map2.roads, map2.road_lengths)

print(a.heur)

#a.shortest_path(0, 12)

h = [366, 374, 329, 380, 244, 241, 242, 253, 193, 160, 176, 100, 0]


for i in range(12):
    print(a.heur[i][12], h[i], a.heur[i][12]/ h[i])


