import M
import math
from queue import PriorityQueue       

def shortest_path(roads, intersections,start,goal):
    print("shortest path called")
    
    # Creating varible helpers
    start_cords = intersections[start]
    goal_cords = intersections[goal]

    # Initialize both open and closed list
    G = {}
    F = {}
 
    #Initialize starting values
    G[start] = 0 

    # Calculating heuristic at starting point
    x = (start_cords[0] - goal_cords[0])**2
    y = (start_cords[1] - goal_cords[1])**2
    heuristic_start = math.sqrt(x + y)
    F[start] = heuristic_start
    
    # Initialize path of route
    path = []
    
    # Initialize sets to check nodes
    open_set = set()
    open_set.add(start)
    closed_set = set()
    came_from = {}

    while len(open_set) > 0:

        #Get the node in the open list with the lowest F score
        current = None
        current_f_score = None

        for node in open_set:
            if current is None or F[node] < current_f_score:
                current_f_score = F[node]
                current = node
 
        #Check if we have reached the goal
        if current == goal:
            #Retrace our route backward
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path #Done!

        #Mark the current vertex as closed
        open_set.remove(current)
        closed_set.add(current)
            
        for next in roads[current]:

            if next in closed_set: 
                continue

            candidateG = G[current] + + math.sqrt(((intersections[next][0] - intersections[current][0]) ** 2) + ((intersections[next][1] - intersections[current][1]) ** 2))
 
            if next not in open_set:
                open_set.add(next) #Discovered a new vertex
            elif candidateG >= G[next]:
                continue #This G score is worse than previously found
 
            #Adopt this G score
            came_from[next] = current
            G[next] = candidateG

            xVal = (intersections[next][0] - intersections[goal][0])**2
            yVal = (intersections[next][1] - intersections[goal][1])**2

            heuristic = math.sqrt(xVal + yVal)

            H = heuristic
            F[next] = G[next] + H


        
#print(shortest_path(M.roads,M.intersections, 8, 24))
path = shortest_path(M.roads,M.intersections, 8, 24)
if path == [8, 14, 16, 37, 12, 17, 10, 24]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)




