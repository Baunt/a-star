from graph import *

class ReadData:
    def __init__(self):
        self.graph = readGraph("data/USA-road-d.NY.gr")
        self.coordinate = readCoordinates("data/USA-road-d.NY.co")

    def getGraphs(self):
        graphs = self.graph
        return graphs

    def getCoordinates(self):
        coordinates = self.coordinate
        return coordinates