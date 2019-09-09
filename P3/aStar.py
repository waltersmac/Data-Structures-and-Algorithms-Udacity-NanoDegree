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
    
    
    # Create start and end node
    start_node = Node(start, (start_cords[0],start_cords[1]))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(start, (goal_cords[0],goal_cords[1]))
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    
    
    # 
    while len(open_list) > 0:
        
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        current_pos = start
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                current_pos = item.parent
                #print(current_pos)
                
                

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        print(open_list)

        # Found the goal
        path = []
        path.append(start)
        print(path)
        
        if current_node == end_node:
            current = current_node
            while current is not None:
                print(current_node.position)

        
        # Generate children
        children = []

        for new_position in roads[start]:

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
      
            # Create the f, g, and h values
            child.g = current_node.g + math.sqrt(((child.position[0] - current_node.position[0]) ** 2) + ((child.position[1] - current_node.position[1]) ** 2))
            child.h = math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


               
        
        


        

path = shortest_path(M.roads,M.intersections, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)


