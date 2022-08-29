from .AGraph import AGraph

class Graph_singular(AGraph):
    """ 1 city, no roads"""
    def __init__(self):

        cities = {
            0: [
                0,
                0
            ]
        }
        
        roads = [ [] ]
       
        super().__init__(cities, roads)
