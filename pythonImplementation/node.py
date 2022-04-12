
class Node(object):

    def __init__(self,x,y):
        "potentially add quadrents"
        self.x = x
        self.y = y
        self.degree = 0
        self.orderVisited = 0
        self.visited = False
        self.nextNode = None

    def addNeighbor(self,node):
        "adds a node that can be reached from the current node"
        self.degree += 1
        self.neighbors.append(node)



    # print(f"{xStart} | {yStart}")
