# Explanation


### Algorithms:

I've written a simple Dfs (Depth first search) and Djikstra's algorithm for testing.

The main code for A* is in the file 'algo/AStar.py'.

It uses ideas from here : (https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes) to make the Priority Queue.

The basic idea is that if you want to update priority values without re-heapifying, you can store red-herring "removed" Nodes instead.

This means popping off the queue entails checking if you have reached a red-herring node and continuing until you reach a "real" one.

len(self.list) is no longer accurate, so I manually maintain the length of the "real" nodes as self.size.

I found this to be much faster than my original implementation using a plain heap (which needs to be re-heapified)




### Graphs:

Graphs (with from 1 to 1000 vertices) are in the folder 'maps/'

Each Graph extends 'AGraph' (which contains method for finding neighbours etc).

I store a 2d array of pre-computed road lengths and heuristic lengths.

Graph_1000 is randomly generated and each of the 1000 cities has a random position and is randomly connected to between 0 and 50 cities.

Eg.

* road_length[i][j] = length of road from i to j.

* heuristic[i][j] = heuristic length from i to j.


The Romania graph (Graph_12) has the heuristics hardcoded (taken from the udacity video).

The other graphs have them calculated using the straight-line distance sqrt(dx^2 + dy^2).

Graphs 4 and 6 have road_lengths that are longer that the straight line distance, to ensure the heuristic is admissible (never over-esimates)

Note that using the straight-line distance is an admissible heuristic, so A* will give us the correct solution.


-----



# Analysis


To get a bound on the space required note that:

* The Heap only increases in size.

* It can be a maximum size of 'nb', where 'n' is the number of cities and 'b' is the branch factor (average number of neighbours per city).

* This is because each city can be considered a maximum of 'b' times - when its neighbours are popped off the heap.

* So, the heap storage space is O(n) in the worst case.

* I also store the 'visited' hash (O(n)) and the 'lookup' hash (also O(n))




Additionally, I store the 2d arrays mentioned above - road_length[][] and heuristic[][].

* These aren't really additional space used by the algorithm, they are part of the input (in the case of road_lengths).

* Also note that the heuristics could be calculated on the fly rather than being pre-computed, which would remove that array completely.


So overall, the additional memory used by the algorithm as it runs is O(nb).

For most maps considered here 'b' is a constant since cities can only be connected to cities nearby.

If b was of order 'n' (an almost complete graph), this would be O(n^2)

-----


For the running time, note:


* Each edge can be considered a maximum of 2 times.

Edge 'a-b' can be considered by the algorithm once when 'a' is taken off the heap and once when 'b' is taken off.

* Each time an edge is considered we either push onto the heap ( O(log k) where k is the size of the heap).

* In the worst case, k = O(n^2), so this is log(n^2) = 2log(n) = O(n) (this is why the red-herring queue is so powerful)

So the worst-case running time for my A* algorithm is O(ne) where 'n' is the number of cities and 'e' the number of edges.





