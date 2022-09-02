from .AGraph import AGraph

class Graph_5(AGraph):
    """ 4 cities in a square and one in the middle"""

    def __init__(self):

        cities = {
            0: [
                0,
                0
            ],
            1: [
                0,
                4
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
                3,
                4
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
                3
            ]
        ]
        
        super().__init__(cities, roads)
