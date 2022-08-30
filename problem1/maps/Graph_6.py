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
        
        road_lengths = {
           0:{
              1:2,
              2:2,
              4:6,
              5:10
           },
           1:{
              0:2,
              3:2
           },
           2:{
             0:2,
             3:4
           },
           3:{
              1:2,
              2:4,
              5:2
           },
           4:{
              0:6,
              5:2
           },
           5:{
               0:10,
               3:2,
               4:2
             }
        }
                
        super().__init__(cities, roads, road_lengths)
