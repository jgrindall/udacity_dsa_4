from maps.Graph_12_romania import Graph_romania
from maps.Graph_10 import Graph_10
from maps.Graph_40 import Graph_40
from maps.Graph_6 import Graph_6
from maps.Graph_4 import Graph_4


from algo.AStar import AStar
from algo.Dijkstra import Dijkstra
from algo.Dfs import Dfs
from algo.ShortestPath import ShortestPath

graph = Graph_40()
a_star = AStar(graph)
print(a_star.shortest_path(0, 2))

