class Node:
    def __init__(self, city, g_value, h_value):
        self.city = city

        self.g_value = g_value
        self.h_value = h_value
        
        self.removed = False

    def __eq__(self, other):
        # to check if a node exists in the heap we can check if the cities match
        return self.city == other.city
    
    def __gt__(self, other):
        return self.f_value > other.f_value
    
    def __lt__(self, other):
        return self.f_value < other.f_value
    
    @property 
    def f_value(self):
        #f = g + h , a computed property
        return self.g_value + self.h_value

    def __repr__(self):
        """ pretty-print """
        s = "Node:"
        s += "  city: " + str(self.city)
        s += "  f_value: " + str(self.f_value)
        s += "  g_value: " + str(self.g_value)
        s += "  h_value: " + str(self.h_value)
        return s
     
    def __str__(self):
         return self.__repr__()
