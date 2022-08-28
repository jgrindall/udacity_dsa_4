class MinHeap:
    def __init__(self, elements = []):
        self.elements = []
        if len(elements) >= 1:
            self.elements.append(elements[0])
        for element in elements[1:]:
            self.insert(element)
        
    def __swap(self, i, j):
        t = self.elements[i]
        self.elements[i] = self.elements[j]
        self.elements[j] = t

    def __get_child_indices(self, i):
        """ Parent at index 'i' has two children at these indices """
        return [
            2*i + 1,
            2*i + 2
        ]
    
    def get_is_empty(self):
        return self.get_size() == 0
    
    def get_size(self):
        """total size"""
        return len(self.elements)

    def __get_parent_index(self, i):
        """Find the index in the array of the element which is the parent of element[i] """
        return (i - 1)//2
    
    def __get_children(self, i):
        """ get the nodes at the child indices (if they exist) """
        children = []
        num_elements = self.get_size()
        for index in self.__get_child_indices(i):
            if index <= num_elements - 1:
                children.append(self.elements[index]);
        return children
    
    def is_valid(self):
        """ helper function for tests - check that the heap property is satisfied"""
        for i in range(self.get_size()):
            if not self.__check_heap_property(i):
                return False
        return True
    
    def __check_heap_property(self, index):
        """check heap propert is ok at index 'index' """
        elt = self.elements[index]
        children = self.__get_children(index)
        #get the children and find ones that are wrong
        incorrect_children = list(filter(lambda child: elt > child, children))
        return len(incorrect_children) == 0;
    
    def heapify(self):
        elts = self.elements
        self.elements = []
        for elt in elts:
            self.insert(elt)
    
    def insert(self, node):
        """ insert new node """
        current_len = len(self.elements)
        # add it
        self.elements.append(node)
        index = current_len
        parent_index = self.__get_parent_index(index)
        # cheeck heap property is ok
        while parent_index >= 0 and not self.__check_heap_property(parent_index):
            # if not, bubble up
            self.__swap(index, parent_index)
            index = parent_index
            if parent_index == 0:
                # we have set the root
                parent_index = -1
            else:
                # keep going
                parent_index = self.__get_parent_index(parent_index)
        
    def get(self):
        """ get the top (min) element """
        num_elements = self.get_size()
        if num_elements == 0:
            return None
        return self.elements[0]
    
    def get_by_key(self, key):
        for elt in self.elements:
            if elt.key == key:
                return elt
        return None
    
    def remove(self):
        """ remove the top (min) element """
        num_elements = self.get_size()
        if num_elements == 0:
            return None
        else:
            root = self.elements[0]
            last = self.elements[-1]
            self.elements[0] = last
            self.elements.pop()
            if len(self.elements) == 0:
                return root
            else:
                # bubble down
                index = 0;
                while not self.__check_heap_property(index):
                    children = self.__get_children(index);
                    if len(children) == 0:
                        raise ValueError("heap property failed");
                    else:
                        #decide which to use
                        child_index = None
                        num_children = len(children)
                        child_indices = self.__get_child_indices(index)
                        if num_children == 1 or (num_children == 2 and children[0] < children[1]):
                            # left child
                            child_index = child_indices[0]
                        else:
                            # right child
                            child_index = child_indices[1]
                        self.__swap(index, child_index)
                        index = child_index
                return root
        
    def __repr__(self):
        elts = [str(elt) for elt in self.elements]
        elts = "\n ".join(elts)
        return "MinHeap:\n " + elts
     
    def __str__(self):
         return self.__repr__()

