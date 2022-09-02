from .AGraph import AGraph

class Graph_6(AGraph):
    """ 6 cities"""

    def __init__(self):

        cities = {
            0: [
                0,
                1
            ],
            1: [
                1,
                2
            ],
            2: [
                1,
                1
            ],
            3: [
                2,
                1
            ],
            4: [
                0,
                0
            ],
            5:[
                2,
                0
            ]
        }

        roads = [
            [
                1,
                2,
                4,
                5
            ],
            [
                0,
                3
            ],
            [
                0,
                3
            ],
            [
                1,
                2,
                5
            ],
            [
                0,
                5
            ],
            [
                0,
                3,
                4
            ]
        ]

        super().__init__(cities, roads)
