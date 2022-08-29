from .AGraph import AGraph

class Graph_simple(AGraph):
    """ 4 cities in a square and one in the middle"""

    def __init__(self):

        cities = {
            0: [
                0,
                0
            ],
            1: [
                2,
                0
            ],
            2: [
                2,
                2
            ],
            3: [
                0,
                2
            ],
            4: [
                1,
                1
            ]
        }

        roads = [
            [
                1,
                3
            ],
            [
                0,
                4
            ],
            [
                # no roads from 2
            ],
            [
                0,
                4
            ],
            [
                0,
                1,
                2
            ]
        ]
        
        road_lengths = {
           0:{
              1:15,
              3:50,
              4:30
           },
           1:{
              0:15,
              4:10
           },
           2:{
             
           },
           3:{
              0:50,
              4:20
           },
           4:{
              0:30,
              1:10,
              3:20
           }
        }
                
        super().__init__(cities, roads, road_lengths)
