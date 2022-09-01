
import time
import random

from maps import Graph_1000, Graph_40, Graph_10, Graph_6, Graph_4, Graph_2, Graph_1
from algo import AStar, Dijkstra

num_runs = 100

graphs = [Graph_1(), Graph_2(), Graph_4(), Graph_6(), Graph_10(), Graph_40(), Graph_1000()]
num_cities = [1, 2, 4, 6, 10, 40, 1000]

for i in range(0, len(graphs)):
    graph = graphs[i]
    dijk = Dijkstra(graph)
    start_time = time.time()
    elapsed = 0
    for n in range(num_runs):
       a = random.randint(0, num_cities[i] - 1)
       b = random.randint(0, num_cities[i] - 1)
       p = dijk.shortest_path(a, b)
    elapsed = time.time() - start_time
    print("dijkstra", num_cities[i], ":\t\t", elapsed * 1000, "msecs")



for i in range(0, len(graphs)):
    graph = graphs[i]
    a_star = AStar(graph)
    start_time = time.time()
    elapsed = 0
    for n in range(num_runs):
       a = random.randint(0, num_cities[i] - 1)
       b = random.randint(0, num_cities[i] - 1)
       p = a_star.shortest_path(a, b)
    elapsed = time.time() - start_time
    print("a_star", num_cities[i], ":\t\t", elapsed * 1000, "msecs")


