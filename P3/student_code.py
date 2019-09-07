import math
from collections import defaultdict

def heuristic(x1,y1,x2,y2):
    x = x2 - x1
    y = y2 - y1
    
    est_distance = math.sqrt((x**2)+(y**2))
    
    return est_distance
    
def neigbor_weight(x1,y1,x2,y2):
    x = x2 - x1
    y = y2 - y1
    
    distance = math.sqrt((x**2)+(y**2))
    
    return distance

def reconstruct_path(cameFrom, current):
    total_path = {current}
    while current in cameFrom.Keys:
        current = cameFrom[current]
        total_path.prepend(current)
    return total_path


def fScore_min(open_set):
    values_sorted = sorted(open_set)
    
    return values_sorted[0]

def shortest_path(M,start,goal):
    print("shortest path called")
    
    heuristic_dist = {}
    start_cords = M.intersections[start]
    intersections = M.intersections
    
    for key,value in intersections.items():
        heuristic_dist[key] = heuristic(start_cords[0],start_cords[1],value[0],value[1])
        
    #The open and closed sets
    open_set = set(start)
    closed_set = set()
    
    came_from = {}
    
    gScore = {}
    gScore[start] = 0

    
    fScore = {}
    fScore[start] = heuristic_dist[start]
    
    while open_set: 
        
        current = fScore_min(open_set)
        return current
        
        if current == goal:
            return reconstruct_path(start, current)

        open_set.remove(current)
        closed_set.add(current)
        
        for neighbor in current:
            
            if neighbor in closed_set: 
                continue
            
            tentative_gScore = gScore[current] + neigbor_weight(M.intersections[M.roads[current]], M.intersections[M.roads[neighbor]])
        
            if tentative_gScore < gScore[neighbor]:
                
                came_from[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + heuristic_dist[neighbor]
                
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return came_from
    
                