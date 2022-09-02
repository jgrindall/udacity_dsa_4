## Running the project:

Note: python3 -> 'py' for Windows


To run the main file:

*  cd problem1 & python3 problem_1.py



To run the tests:

*  cd problem1 & python3 -m doctest -v tests.txt



To see the timing of A* vs Dijkstra

*  cd problem1 & python3 timing_1.py


dijkstra 1 :             0.0 msecs
dijkstra 2 :             0.9799003601074219 msecs
dijkstra 4 :             2.941608428955078 msecs
dijkstra 6 :             2.9363632202148438 msecs
dijkstra 10 :            1.9578933715820312 msecs
dijkstra 40 :            24.489641189575195 msecs
dijkstra 1000 :          12176.709651947021 msecs

a_star 1 :               0.9815692901611328 msecs
a_star 2 :               0.9782314300537109 msecs
a_star 4 :               2.938985824584961 msecs
a_star 6 :               1.9583702087402344 msecs
a_star 10 :              2.9387474060058594 msecs
a_star 40 :              10.773897171020508 msecs
a_star 1000 :            326.6105651855469 msecs