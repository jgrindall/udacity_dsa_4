from Algorithm import Algorithm

class Dfs(Algorithm):
    
    def __init__(self, cities, roads, road_lengths = None):
        super().__init__(cities, roads, road_lengths)


    def shortest_path(self, start, goal):
       if start == goal:
           pass
       
       stack = [] 
       visited = {}
       
       stack.push(start)
       while len(stack) >= 1:
           city = stack.pop()
           neighbours = self.get_neighbours(city)
           for neighbour in neighbours:
               stack.push(stack)
           
   