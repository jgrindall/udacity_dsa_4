from Algorithm import Algorithm

class Dijkstra(Algorithm):
    
    def __init__(self, cities, roads, road_lengths = None):
        super().__init__(cities, roads, road_lengths)


    def shortest_path(self, start, goal):
        #https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
        
        cities = self.cities.keys()
        unvisited_nodes = list(cities)
 
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        shortest_path = {}
     
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}
     
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        max_value = float('inf')
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        
        # However, we initialize the starting node's value with 0   
        shortest_path[start] = 0
        
        
        def get_next_node():
            current_min_node = unvisited_nodes[0]
            current_min = shortest_path[current_min_node]
            for node in unvisited_nodes[1:]:
                if shortest_path[node] < current_min:
                    current_min_node = node
                    current_min = shortest_path[node]
            return current_min_node
        
        
        
        # The algorithm executes until we visit all nodes
        while len(unvisited_nodes) >= 1:
            # The code block below finds the node with the lowest score
            current_min_node = get_next_node()
            # The code block below retrieves the current node's neighbors and updates their distances
            neighbours = self.get_neighbours(current_min_node)
            for neighbor in neighbours:
                val = shortest_path[current_min_node] + self.get_road_length(current_min_node, neighbor)
                if val < shortest_path[neighbor]:
                    shortest_path[neighbor] = val
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node
     
            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)


        return {
            "path": Algorithm.walk_backwards(start, goal, previous_nodes),
            "length": shortest_path[goal]
        }