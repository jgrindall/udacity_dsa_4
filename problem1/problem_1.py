from maps.Graph_romania import Graph_romania
from maps.Graph_10 import Graph_10
from maps.Graph_40 import Graph_40

from algo.AStar import AStar
from algo.Dijkstra import Dijkstra
from algo.Dfs import Dfs

def p(graph, start, goal):
    dfs = Dfs(graph)
    print(dfs.shortest_path(start, goal))
    
    dijk = Dijkstra(graph)
    print(dijk.shortest_path(start, goal))
    
    a_star = AStar(graph)
    print(a_star.shortest_path(start, goal))
    

graph_romania = Graph_romania()

p(graph_romania, 0, 12)
p(Graph_10(), 0, 4)
p(Graph_40(), 5, 34)
p(Graph_40(), 8, 24)
