class Node:
    def __init__(self, city, g_value, h_value):
        self.city = city

        #f = g + h 
        self.g_value = g_value
        self.h_value = h_value

    def __eq__(self, other):
        return self.city == other.city
    
    def __gt__(self, other):
        return self.f_value > other.f_value
    
    @property 
    def f_value(self):
        return self.g_value + self.h_value
    
    @property 
    def key(self):
        return self.city
    
    def __repr__(self):
        s = "Node:"
        s += "  city: " + str(self.city)
        s += "  f_value: " + str(self.f_value)
        s += "  g_value: " + str(self.g_value)
        s += "  h_value: " + str(self.h_value)
        return s
     
    def __str__(self):
         return self.__repr__()
