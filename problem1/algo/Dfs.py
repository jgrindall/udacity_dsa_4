from .AAlgorithm import AAlgorithm
from .ShortestPath import ShortestPath

class Dfs(AAlgorithm):
    
    def __init__(self, graph):
        super().__init__(graph)


    def shortest_path(self, start, goal):
        if start == goal:
            return ShortestPath(0.0, [start])
        
        """ else, do a depth-first-search"""
        
        #store ones we find
        found_paths = []
        
        # mark which we have explored to avoid cycles
        visited = {}

        #current path being constructed
        path = []

        def dfs(a, b):
            nonlocal visited
            nonlocal found_paths
            nonlocal path

            visited[a] = True
            path.append(a)

            if a == b:
                # We found one
                found_paths.append(path.copy())
            neighbours = self.graph.get_neighbours(a)
            for neighbour in neighbours:
                if neighbour not in visited:
                    dfs(neighbour, b)
                
            path.pop()
            del visited[a]


        dfs(start, goal)

        # if we didn't find any at all, return None
        if len(found_paths) == 0:
           return ShortestPath()

        def get_path_length(path):
            """ get the length of a path. Eg [0, 4, 7]-> road(0, 4) + road(4, 7) """
            if len(path) <= 1:
                return 0
            length = 0
            city0 = path[0]
            for city1 in path[1:]:
                length += self.graph.get_road_length(city0, city1)
                city0 = city1
            return length

        # simple scan through all of the possible paths, to find the shortest
        min_path = None
        min_path_length = float('inf')
        for path in found_paths:
            path_length = get_path_length(path) 
            if path_length < min_path_length:
               min_path_length = path_length
               min_path = path
        
        
        return ShortestPath(float(min_path_length), min_path)
