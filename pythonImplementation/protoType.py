""""
find the tile closest to the edge 
"""
from node import *

def calulateDifference(node):
    xDifference = 0
    yDifference = 0
    
    if (node.x < 4):
        xDifference = 4 - node.x
    else:
        xDifference = 8 - node.x

    if (node.y < 4):
        yDifference = 4 - node.y
    else:
        yDifference = 8 - node.y

    print(f"difference: {xDifference},{yDifference}")
    return (xDifference,yDifference)

def findClosestToWall(node1,node2):
    """"
    check the x values 
    check the y values
    """
    xdifferece1,ydifferece1 = calulateDifference(node1)
    xdifferece2,ydifferece2 = calulateDifference(node2)
    if (xdifferece1 != xdifferece2):
        if (xdifferece1 < xdifferece2):
            return node1
        else:
            return node2
    else:
        if (ydifferece1 < ydifferece2):
            return node1
        else:
            return node2

first = Node(2,6)
second = Node(7,6)
calulateDifference(first)
closest = findClosestToWall(first,second)
print(f"closest: {closest.x},{closest.y}")