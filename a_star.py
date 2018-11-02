
from graph import *
from read_data import ReadData
import numpy as np
import heapq
from scipy.spatial import distance

# Read graph data and coordinates data (to be implemented)

###########################################
########## A* implementation ##############
###########################################

#"----------------------------------------------"
#"longitude, latatitude = coordinates(node)"
#"h,w = angels2centimeters(latitude, longitude)"
#"----------------------------------------------"

# Priority queue definition
# class PriorityQueue:
#     def __init__(self, f):
#         self.elements = []
#         self.f = f

#     def empty(self):
#         return len(self.elements) == 0

#     def included(self, item):
#         return item in self.elements

#     def put(self, item):
#         self.elements.append(item)

#     def get(self):
#         e_min = min(self.elements, key=lambda e:self. [e])
#         self.elements.pop(self.elements.index(e_min))
#         return e_min

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def angles2centimeters(la, lo):
    """
    :param la: latitude
    :param lo: longitude
    :return: new orthogonal grid centered around NYC
    """
    
    radius = 6300 * 1e4  # cm. While 6369.053*1e4 is more realistic, this could fail the heuristic
    la_mean = 40794234.  # 1e-6 degree
    lo_mean = -74016939.  # 1e-6 degree
    
    h = radius * np.radians((la - la_mean) / 1e6)
    w = radius * np.cos(np.radians(la / 1e6)) * np.radians((lo - lo_mean) / 1e6)
    
    return h, w


def h(pos1,pos2,coordinate):
    """
    Heuristic function (to be implemented)
    convert coordinates from degree to cm (def angle2cm)
    """
    #Manhattan distance
    (x1,y1) = coordinate[pos1]
    (x2,y2) = coordinate[pos2]

    h1,w1 = angles2centimeters(y1, x1)
    h2,w2 = angles2centimeters(y2, x2)
    return abs(w1-w2) + abs(h1-h2)

# A* algorithm (to be implemented)
def a_star_search(graph,coordinate,start,goal):
    """
    :param graph:
    :param start:
    :param goal:
    :return: The path and total length
    """
    # open_queue = PriorityQueue()
    # open_queue.put(start, 0)
    # closed = set()
    # came_from = {}
    # cost_so_far = {}
    # came_from[start] = None
    # cost_so_far[start] = 0

    # while not open_queue.empty():
    #     current = open_queue.get()
        
    #     if current == goal:
    #         break
        
    #     closed.add(current)
    #     currentVertex = graph.getVertex(current)
    #     i = 0
    #     for next in currentVertex.neighbors:
    #         new_cost = cost_so_far[current] + currentVertex.weights[i]
    #         if next not in cost_so_far or new_cost < cost_so_far[next]:
    #             cost_so_far[next] = new_cost
    #             f = new_cost + h(next,goal, coordinate)
    #             open_queue.put(next, f)
    #             came_from[next] = current 
    #             i = i + 1
    # return closed, cost_so_far
    openset = set()
    openset.add(start)
    closedset = set()
    cameFrom = {}
    cameFrom[start] = None
    g = {}
    g[start] = 0
    f = {}
    f[start] = 0
    while openset:
        current = min(openset)
        if current == goal:
            break
        openset.remove(current)
        closedset.add(current)        
        currentVertex = graph.getVertex(current)
        for i in range(0, len(currentVertex.neighbors)):
            if currentVertex.neighbors[i] in closedset:
                continue   
            tentative_g_score = currentVertex.weights[i] + g[current]
            if currentVertex.neighbors[i] not in openset:
                openset.add(currentVertex.neighbors[i])
            elif tentative_g_score >= currentVertex.weights[i]:
                continue
            cameFrom[currentVertex.neighbors[i]] = current
            heuristic = h(currentVertex.neighbors[i],goal,coordinate)
            g[currentVertex.neighbors[i]] = tentative_g_score
            f_result = tentative_g_score + heuristic
            f[currentVertex.neighbors[i]] = f_result
    return cameFrom, f
        # for neighbor in currentVertex.neighbors:            
        #     if neighbor in closedset:
        #         continue       
        #     tentative_g_score = sum(g) + currentVertex.weights[counter]
        #     if neighbor not in openset:
        #         openset.add(neighbor)
        #     elif tentative_g_score >= currentVertex.weights[counter]:
        #         continue
        #     cameFrom.add(current)
        #     g.add(tentative_g_score)
        #     f.add(sum(g) + h(neighbor,goal,coordinate))
    
