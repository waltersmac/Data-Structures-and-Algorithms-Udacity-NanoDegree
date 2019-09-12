import M
import math

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
       

def shortest_path(roads, intersections,start,goal):
    print("shortest path called")
    
    # Creating varible helpers
    start_cords = intersections[start]
    goal_cords = intersections[goal]
    
    print("start co-ords",(start_cords[0],start_cords[1]))
    # Create start and end node
    start_node = Node(start, (start_cords[0],start_cords[1]))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(goal, (goal_cords[0],goal_cords[1]))
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    

    #
    path = [] 
    
    # 
    while len(open_list) > 0:
        
        current = min(open_list, key=lambda o:o.g + o.h)
        print(current)

        # Get the current node
        current_node = open_list[0]
        print(current_node.parent)
        current_index = 0
        for index, item in enumerate(open_list):
            
            if item.f < current_node.f or item.f == 0:
            	current_node = item
            	current_index = index       

                

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        
        if current_node.parent == end_node.parent:
        	path.append(current_node.parent)
        	return path

        else:
        	path.append(current_node.parent)
            

        
        # Generate children
        children = []
        
        for new_position in roads[current_node.parent]:

            # Get node position
            node_position = (intersections[new_position][0], intersections[new_position][1])

            # Create new node
            new_node = Node(new_position, node_position)

            # Append
            children.append(new_node)

            
        # Loop through children
        for child in children:


            # Child is on the closed list
            if child in closed_list:
                continue

            #print("current pos",current_node.parent,current_node.position[0],current_node.position[1],"child pos", child.position[0],child.position[1])
            # Create the f, g, and h values
            #print(((child.position[0] - current_node.position[0]) ** 2) + ((child.position[1] - current_node.position[1]) ** 2))
            if child in open_list:

                child.g = current_node.g + math.sqrt(((child.position[0] - current_node.position[0])**2) + ((child.position[1] - current_node.position[1])**2))
            
                xVal = ((child.position[0] - end_node.position[0])**2)
                yVal = ((child.position[1] - end_node.position[1])**2)
                child.h = math.sqrt(xVal + yVal)

                child.f = child.g + child.h

            print("child g", child.g, "child h", child.h,"child f", child.f)
            

            # Add the child to the open list
            open_list.append(child)
        
        

path = shortest_path(M.roads,M.intersections, 8, 24)
if path == [8, 14, 16, 37, 12, 17, 10, 24]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)




