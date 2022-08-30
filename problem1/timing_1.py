#Test tiny

>>> from maps.Graph_2 import Graph_2
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.ShortestPath import ShortestPath
>>> from algo.Dfs import Dfs
>>> graph = Graph_2()
>>> expected_ans = ShortestPath(1.0, [0, 1])
>>> dfs = Dfs(graph)
>>> dfs.shortest_path(0, 1) == expected_ans
True
>>> dijk = Dijkstra(graph)
>>> dijk.shortest_path(0, 1) == expected_ans
True
>>> a_star = AStar(graph)
>>> a_star.shortest_path(0, 1) == expected_ans
True
>>> expected_ans = ShortestPath(0.0, [0])
>>> dfs.shortest_path(0, 0) == expected_ans
True
>>> dijk.shortest_path(0, 0) == expected_ans
True
>>> a_star.shortest_path(0, 0) == expected_ans
True


#Test tiny - start equals goal
>>> from maps.Graph_2 import Graph_2
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_2()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> expected_ans = ShortestPath(0.0, [0])
>>> dfs.shortest_path(0, 0) == expected_ans
True
>>> dijk.shortest_path(0, 0) == expected_ans
True
>>> a_star.shortest_path(0, 0) == expected_ans
True



#Test singular - one city
>>> from maps.Graph_1 import Graph_1
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_1()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> expected_ans = ShortestPath(0.0, [0])
>>> dfs.shortest_path(0, 0) == expected_ans
True
>>> dijk.shortest_path(0, 0) == expected_ans
True
>>> a_star.shortest_path(0, 0) == expected_ans
True



#Test disconnected
>>> from maps.Graph_2_disconnected import Graph_2_disconnected
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_2_disconnected()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> expected_ans = ShortestPath(0.0, [0])
>>> dfs.shortest_path(0, 0) == expected_ans
True
>>> dijk.shortest_path(0, 0) == expected_ans
True
>>> a_star.shortest_path(0, 0) == expected_ans
True
>>> expected_ans = ShortestPath()
>>> dfs.shortest_path(1, 0) == expected_ans
True
>>> dijk.shortest_path(1, 0) == expected_ans
True
>>> a_star.shortest_path(1, 0) == expected_ans
True
>>> expected_ans = ShortestPath()
>>> dfs.shortest_path(0, 1) == expected_ans
True
>>> dijk.shortest_path(0, 1) == expected_ans
True
>>> a_star.shortest_path(0, 1) == expected_ans
True




#Test Romania map from lectures, Arad->Arad
>>> from maps.Graph_12_romania import Graph_12_romania
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_12_romania()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> expected_ans = ShortestPath(0.0, [0])
>>> dfs.shortest_path(0, 0) == expected_ans
True
>>> dijk = Dijkstra(graph)
>>> dijk.shortest_path(0, 0) == expected_ans
True
>>> a_star = AStar(graph)
>>> a_star.shortest_path(0, 0) == expected_ans
True




#Test Romania map from lectures, Arad->Bucharest
>>> from maps.Graph_12_romania import Graph_12_romania
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_12_romania()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> expected_ans = ShortestPath(418.0, [0, 7, 8, 11, 12])
>>> dfs.shortest_path(0, 12) == expected_ans
True
>>> dijk = Dijkstra(graph)
>>> dijk.shortest_path(0, 12) == expected_ans
True
>>> a_star = AStar(graph)
>>> a_star.shortest_path(0, 12) == expected_ans
True





#Test Simple map
>>> from maps.Graph_4 import Graph_4
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_4()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> expected_ans = ShortestPath(0.0, [0])
>>> dfs.shortest_path(0, 0) == expected_ans
True
>>> dijk = Dijkstra(graph)
>>> dijk.shortest_path(0, 0) == expected_ans
True
>>> a_star.shortest_path(0, 0) == expected_ans
True
>>> expected_ans =ShortestPath(15.0, [0, 1])
>>> dfs.shortest_path(0, 1) == expected_ans
True
>>> dijk.shortest_path(0, 1) == expected_ans
True
>>> a_star = AStar(graph)
>>> a_star.shortest_path(0, 1) == expected_ans
True
>>> expected_ans = ShortestPath()
>>> dfs.shortest_path(0, 2) == expected_ans
True
>>> dijk.shortest_path(0, 2) == expected_ans
True
>>> a_star.shortest_path(0, 2) == expected_ans
True
>>> expected_ans = ShortestPath(45.0, [0, 1, 4, 3])
>>> dfs.shortest_path(0, 3) == expected_ans
True
>>> dijk.shortest_path(0, 3) == expected_ans
True
>>> a_star.shortest_path(0, 3) == expected_ans
True
>>> expected_ans = ShortestPath(25.0, [0, 1, 4])
>>> dfs.shortest_path(0, 4) == expected_ans
True
>>> dijk.shortest_path(0, 4) == expected_ans
True
>>> a_star.shortest_path(0, 4) == expected_ans
True



#Test Map 6
>>> from maps.Graph_6 import Graph_6
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_6()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> failed_tests = []
>>> for i in range(0, 6):
...   for j in range(0, 6):
...      a1 = dfs.shortest_path(i, j)
...      a2 = dijk.shortest_path(i, j)
...      a3 = a_star.shortest_path(i, j)
...      if a1.length != a2.length or a2.length != a3.length:
...         failed_tests.append([i, j, a1, a2, a3])
>>> print(failed_tests)
[]



#Test Map 10
>>> from maps.Graph_10 import Graph_10
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.Dfs import Dfs
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_10()
>>> dfs = Dfs(graph)
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> failed_tests = []
>>> for i in range(0, 10):
...   for j in range(0, 10):
...      a1 = dfs.shortest_path(i, j)
...      a2 = dijk.shortest_path(i, j)
...      a3 = a_star.shortest_path(i, j)
...      if a1.length != a2.length or a2.length != a3.length:
...         failed_tests.append([i, j, a1, a2, a3])
>>> print(failed_tests)
[]




#Test Map 40
>>> from maps.Graph_40 import Graph_40
>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.ShortestPath import ShortestPath
>>> graph = Graph_40()
>>> dijk = Dijkstra(graph)
>>> a_star = AStar(graph)
>>> failed_tests = []
>>> for i in range(0, 40):
...   for j in range(0, 40):
...      a1 = dijk.shortest_path(i, j)
...      a2 = a_star.shortest_path(i, j)
...      if a1.length != a2.length:
...         failed_tests.append([i, j, a1, a2])
>>> print(failed_tests)
[]





#Test - times
>>> import time
>>> import random
>>> from maps.Graph_40 import Graph_40
>>> from maps.Graph_10 import Graph_10
>>> from maps.Graph_6 import Graph_6
>>> from maps.Graph_4 import Graph_4
>>> from maps.Graph_2 import Graph_2
>>> from maps.Graph_1 import Graph_1

>>> from algo.AStar import AStar
>>> from algo.Dijkstra import Dijkstra
>>> from algo.ShortestPath import ShortestPath

>>> num_runs = 10000

>>> graphs = [Graph_1(), Graph_2(), Graph_4(), Graph_6(), Graph_10(), Graph_12_romania(), Graph_40()]
>>> num_cities = [1, 2, 4, 6, 10, 12, 40]
>>> for i in range(0, len(graphs)):
...   graph = graphs[i]
...   dijk = Dijkstra(graph)
...   start_time = time.time()
...   elapsed = 0
...   for n in range(num_runs):
...      a = random.randint(0, num_cities[i])
...      b = random.randint(0, num_cities[i])
...      p = dijk.shortest_path(a, b)
...   elapsed = time.time() - start_time
...   print("dijkstra", num_cities[i], elapsed * 1000, "msecs")








