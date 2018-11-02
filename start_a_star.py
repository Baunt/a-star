from a_star import *
from read_data import ReadData

graph = ReadData()
result = a_star_search(graph.getGraphs(),graph.getCoordinates(),169781,79088)
print(result)