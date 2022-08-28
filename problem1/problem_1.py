from maps.map_romania import Map as map_romania
from maps.map_10 import Map as map_10
from maps.map_40 import Map as map_40
from AStar import AStar
from Dijkstra import Dijkstra


def p(map, start, goal):
    a = AStar(map.cities, map.roads, map.road_lengths, map.heur)
    
    print(a.shortest_path(start, goal))
    
    d = Dijkstra(map.cities, map.roads, map.road_lengths)
    
    print(d.shortest_path(start, goal))
    
    
p(map_romania, 0, 12)
p(map_10, 0, 4)
p(map_40, 5, 34)
p(map_40, 8, 24)
