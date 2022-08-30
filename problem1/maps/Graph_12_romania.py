from .AGraph import AGraph

class Graph_12_romania(AGraph):
    """ The graph used in the videos"""
    def __init__(self):

        cities = {
            0: [
                119,   #Arad
                195
            ],
            1: [
                152,
                115
            ],
            2: [
                124,
                363
            ],
            3: [
                204,
                28
            ],
            4: [
                265,
                426
            ],
            5: [
                274,
                505
            ],
            6: [
                269,
                586
            ],
            7: [
                358,
                270
            ],
            8: [
                409,
                367
            ],
            9: [
                446,
                609
            ],
            10: [
                561,
                292
            ],
            11: [
                584,
                455
            ],
            12: [
                737,  #Bucharest
                531
            ]
        }

        roads = [
            [
                1,
                2,
                7
            ],
            [
                0,
                3
            ],
            [
                0,
                4
            ],
            [
                1,
                7
            ],
            [
                2,
                5
            ],
            [
                4,
                6
            ],
            [
                5,
                9
            ],
            [
                0,
                3,
                8,
                10
            ],
            [
                7,
                9,
                11
            ],
            [
                6,
                8,
                11
            ],
            [
                7,
                12
            ],
            [
                8,
                9,
                12
            ],
            [
                10,
                11
            ]
        ]
        
        road_lengths = {
           0:{
              1:75,
              2:118,
              7:140
           },
           1:{
              0:75,
              3:71
           },
           2:{
              0:118,
              4:111
           },
           3:{
              1:71,
              7:151
           },
           4:{
              2:111,
              5:70
           },
           5:{
              4:70,
              6:75
           },
           6:{
              5:75,
              9:120
           },
           7:{
              0:140,
              3:151,
              8:80,
              10:99
           },
           8:{
              7:80,
              9:146,
              11:97
           },
           9:{
              6:120,
              8:146,
              11:138
           },
           10:{
              7:99,
              12:211
           },
           11:{
              8:97,
              9:138,
              12:101
           },
           12:{
              10:211,
              11:101
           }
        }
        
        heuristics = {}
        
        #we only need the heuristic lengths from 'i' to 12 - from each city to Bucharest
        for i in range(13):
            heuristics[i] = {}
            for j in range (13):
                heuristics[i][j] = None
        
        heuristics[0][12] = 366
        heuristics[1][12] = 374
        heuristics[2][12] = 329
        heuristics[3][12] = 380
        heuristics[4][12] = 244
        heuristics[5][12] = 241
        heuristics[6][12] = 242
        heuristics[7][12] = 253
        heuristics[8][12] = 193
        heuristics[9][12] = 160
        heuristics[10][12] = 176
        heuristics[11][12] = 100
        heuristics[12][12] = 0
        
        super().__init__(cities, roads, road_lengths, heuristics)
