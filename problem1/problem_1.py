from maps import Graph_1000, Graph_40, Graph_12_romania, Graph_10, Graph_6, Graph_4, Graph_2, Graph_1
from algo import Dfs, AStar, Dijkstra


graph = Graph_40()
a_star = AStar(graph)


a2 = a_star.shortest_path(0, 2)
print(a2)

