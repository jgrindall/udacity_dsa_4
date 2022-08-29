from .AAlgorithm import AAlgorithm

class Dijkstra(AAlgorithm):
    
    def __init__(self, graph):
        super().__init__(graph)


    def shortest_path(self, start, goal):
        unvisited = list(self.graph.cities.keys())
 
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        shortest_path = {}
     
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}
     
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        for node in unvisited:
            shortest_path[node] = float('inf')
        
        # However, we initialize the starting node's value with 0   
        shortest_path[start] = 0
        

        def get_next_node():
            """ find the next node to visit """
            min_node = unvisited[0]
            min_value = shortest_path[min_node]
            for node in unvisited[1:]:
                if shortest_path[node] < min_value:
                    min_node = node
                    min_value = shortest_path[node]
            return min_node

        
        # The algorithm executes until we visit all nodes
        while len(unvisited) >= 1:
            node = get_next_node()
            neighbours = self.graph.get_neighbours(node)
            for neighbour in neighbours:
                val = shortest_path[node] + self.graph.get_road_length(node, neighbour)
                if val < shortest_path[neighbour]:
                    shortest_path[neighbour] = val
                    # We also update the best path to the current node
                    previous_nodes[neighbour] = node
     
            # After visiting its neighbors, we mark the node as "visited"
            unvisited.remove(node)


        return {
            "length": shortest_path[goal],
            "path": AAlgorithm.walk_backwards(start, goal, previous_nodes)
        }