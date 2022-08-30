class ShortestPath:
    def __init__(self, length = float('inf'), path = None):
        self.length = length
        self.path = path

    def __repr__(self):
        """ pretty-print """
        s = "ShortestPath:"
        s += "  length: " + str(self.length)
        s += "  path: " + str(self.path)
        return s
    
    def __eq__(self, other):
        return self.length == other.length and self.path == other.path
     
    def __str__(self):
         return self.__repr__()