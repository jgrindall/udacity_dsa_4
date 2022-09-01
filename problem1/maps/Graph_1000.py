from .AGraph import AGraph
import random

""" Note this one is random """

class Graph_1000(AGraph):
    
    def __init__(self):
        
        num_cities = 1000
        
        all_cities = list(range(0, num_cities))
        
        min_num_edges_per_city = 0
        max_num_edges_per_city = 50
        
        cities = {}
     
        roads = []
        
        for i in range(num_cities):
            roads.append([])
            cities[i] = [
                #x/y positions
                random.uniform(0, 1),
                random.uniform(0, 1)
            ]
            

        for i in range(num_cities):
            random.shuffle(all_cities)
            num_roads = random.randint(min_num_edges_per_city, max_num_edges_per_city)
            for j in range(num_roads):
                roads[i].append(all_cities[j])
        super().__init__(cities, roads)
