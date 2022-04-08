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
    if (node1.x != node2.x):
        if (node1.x < node2.x):
            return node1
        else:
            return node2
    else:
        if (node1.y < node2.y):
            return node1
        else:
            return node2

print(4 % 0)