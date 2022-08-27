class Map():
    
    def __init__():
        pass
    
    #10 intersections, each identified by an x,y coordinate
    cities = {
        0: [
            119,
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
            737,
            531
        ]
    }


    #roads[i] contains a list of the intersections that intersection i connects to.
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
    
    heur = {
        
     
            0:{None,None,None,None,None,None,None,None,None,None,None,None,366},
            1:{None,None,None,None,None,None,None,None,None,None,None,None,374},
            2:{None,None,None,None,None,None,None,None,None,None,None,None,329},
            3:{None,None,None,None,None,None,None,None,None,None,None,None,380},
            4:{None,None,None,None,None,None,None,None,None,None,None,None,244},
            5:{None,None,None,None,None,None,None,None,None,None,None,None,241},
            6:{None,None,None,None,None,None,None,None,None,None,None,None,242},
            7:{None,None,None,None,None,None,None,None,None,None,None,None,253},
            8:{None,None,None,None,None,None,None,None,None,None,None,None,193},
            9:{None,None,None,None,None,None,None,None,None,None,None,None,160},
            10:{None,None,None,None,None,None,None,None,None,None,None,None,176},
            11:{None,None,None,None,None,None,None,None,None,None,None,None,100},
            12:{None,None,None,None,None,None,None,None,None,None,None,None,0},
            
            
        }
    
    
    road_lengths = {
        0:{1: 72, 2:118, 7:140},
        1:{0:75 , 3: 71},
        2:{0:118 , 4: 111},
        3:{1: 71, 7:151},
        4:{2:111, 5:70},
        5:{4:70, 6:75},
        6:{5:75, 9:120},
        7:{0:140, 3:151, 8:80, 10:99},
        8:{7:80, 9:146, 11:97},
        9:{6:120, 8:146, 11:138},
        10:{7:99, 12:211},
        11:{8:97, 9:138, 12:101},
        12:{10:211, 11:101},
        
    }