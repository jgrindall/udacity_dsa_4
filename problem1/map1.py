class Map():
    
    def __init__():
        pass
    
    #10 intersections, each identified by an x,y coordinate
    cities = {
        0: [
            0.7798606835438107,
            0.6922727646627362
        ],
        1: [
            0.7647837074641568,
            0.3252670836724646
        ],
        2: [
            0.7155217893995438,
            0.20026498027300056
        ],
        3: [
            0.7076566826610747,
            0.3278339270610988
        ],
        4: [
            0.8325506249953353,
            0.02310946309985762
        ],
        5: [
            0.49016747075266878,
            0.5464878695400415
        ],
        6: [
            0.8820353070895344,
            0.6791919587749445
        ],
        7: [
            0.46247219371675077,
            0.6258061621642713
        ],
        8: [
            0.11622158839385677,
            0.11236327488812581
        ],
        9: [
            0.1285377678230034,
            0.3285840695698353
        ]
    }


    #roads[i] contains a list of the intersections that intersection i connects to.
    roads = [
        [
            7,
            6,
            5
        ],
        [
            4,
            3,
            2
        ],
        [
            4,
            3,
            1
        ],
        [
            5,
            4,
            1,
            2
        ],
        [
            1,
            2,
            3
        ],
        [
            7,
            0,
            3
        ],
        [
            0
        ],
        [
            0,
            5
        ],
        [
            9
        ],
        [
            8
        ]
    ]
    
    
    road_lengths = None