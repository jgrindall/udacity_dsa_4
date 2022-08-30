from .AGraph import AGraph

class Graph_2(AGraph):
    """ 2 cities, one road"""
    def __init__(self):

        cities = {
            0: [
                0,
                0
            ],
            1: [
                1,
                0
            ]
        }
        
        roads = [
            [
                1
            ],
            [
                0    
            ]
        ]
       
        super().__init__(cities, roads)
