from .AAlgorithm import AAlgorithm

class Dfs(AAlgorithm):
    
    def __init__(self, graph):
        super().__init__(graph)


    def shortest_path(self, start, goal):
       if start == goal:
           pass
       
       """ do a depth-fikeysrst-search"""
       
       visited = {}
       
       #make two stacks, one for the cities and one for the paths we took
       stack = [start] 
       paths = [[start]]
       
       found_paths = []
       
       while len(stack) >= 1:
           city = stack.pop(0)
           path = paths.pop(0)
           
           # mark as visited to avoid cycles
           visited[city] = True

           if city is goal:
               # We found one
               found_paths.append(path)

           neighbours = self.graph.get_neighbours(city)
           for neighbour in neighbours:
               if neighbour not in visited:
                   stack.append(neighbour)
                   paths.append(path + [neighbour])
                   
       # if we didn't find any at all, return None
       if len(found_paths) == 0:
           return None
       
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
       
        
       # simple scan through all of them to find the shortest
       min_path = None
       min_path_length = float('inf')
       for path in found_paths:
            path_length = get_path_length(path) 
            if path_length < min_path_length:
               min_path_length = path_length
               min_path = path
               
               
               
       return {
            "length": min_path_length,
            "path": min_path
       }