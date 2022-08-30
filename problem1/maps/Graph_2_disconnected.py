from .AGraph import AGraph

class Graph_2_disconnected(AGraph):
    """ 2 cities, disconnected """

    def __init__(self):

        cities = {
            0: [
                0,
                0
            ],
            1: [
                1,
                1
            ]
        }

        roads = [
            [
              
            ],
            [
               
            ]
        ]

        road_lengths = {
           0:{
             
           },
           1:{
             
           }
        }
                
        super().__init__(cities, roads, road_lengths)
