from graph import readGraph
from a_star import a_star_search

graphs = readGraph("data/USA-road-d.NY.gr")
print("FOS")
a_star_search(graphs,0,5)

