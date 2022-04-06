from node import *

""""
create all nodes 
link all nodes 

algorithm:
create the hueristic value of each piece (degree attribute)
update the values after each turn 
mark vistied nodes 
always choose the node with the least degree
"""
class Graph(object):

    def __init__(self,dimension = "8x8"):
        self.dimension = dimension
        self.totalNodes = 0
        self.allNodes = []
        self.connections = dict(())

    def setTotalNodes(self):
        allValues = [int(x) for x in self.dimension.split("x")]
        self.totalNodes = allValues[0] * allValues[1]
    
    def createAllNodes(self,totalNodes = [],x = 0,y = 0,counter = 0):

        if (counter == self.totalNodes):
            return totalNodes
        elif (x > 7):
            x = 0
            print("\n",end="")
            return self.createAllNodes(totalNodes,x,y + 1,counter)
        else:
            newNode = Node(x,y)
            totalNodes.append(newNode)
            print(f"({newNode.x},{newNode.y})",end=" ")
            return self.createAllNodes(totalNodes,x + 1,y,counter + 1)
    def findNode(self,index,x,y,node = None):
        """"
        should find a node with the given x,y values 
        """
        if ((node.x == x) and (node.y == y)):
            return node
        else:
            node = self.allNodes[index]
            return self.findNode(index + 1,x,y,node)
    def findNeighbors(self,originalX,originalY,index,totalNodes):
        """"
        given an x and a y should return a list of all valid nodes from each positions
        used to create a dictionary of nodes 
        """
        xOffsets = (1,-1,1,-1,2,-2,2,-2)
        yOffsets = (2,2,-2,-2,1,1,-1,-1)
        if (index == (len(xOffsets))):
            return totalNodes
        else:
            # create new x and new y 
            # sanitize new x, and y offsets so its withing the gameboard
            newX = originalX + xOffsets[index]
            newY = originalY + yOffsets[index]
            
            if ((newX >= 0) and (newX <= 7)):
                if ((newY >= 0) and (newY <= 7)):
                    # find the node that corrisponds to the x,y
                    newNode = self.findNode(0,newX,newY,Node(0,0))
                    totalNodes.append(newNode)
                    # print(f" \n ({newNode.x},{newNode.y}) location: {newNode}")
        return self.findNeighbors(originalX,originalY,index + 1,totalNodes)
            
    def connectAllNodes(self,x,y,counter):
        """"
        from a given node, it should create an list (arrayList) of legal nodes to visit
        find the current node
        find all nodes that can be visited and add them to a list 
        set the degree of the current node 
        add the current node as a key
        the value will be the list of legal moves
        """
        if (counter == self.totalNodes):
            return 1
        elif (x > 7):
            x = 0
            return self.connectAllNodes(x,y + 1,counter)
        elif (y > 7):
            y = 0
        else:
            currentNode = self.findNode(0,x,y,Node(0,0))
            neighbors = self.findNeighbors(currentNode.x,currentNode.y,0,[])
            currentNode.degree = len(neighbors)
            print(f" \n \n current: ({currentNode.x},{currentNode.y}) location: {currentNode} | counter: {counter} | x: {x} y: {y}")
            for node in neighbors:
                print(f"neighbor: ({node.x},{node.y}) | {node}")
            self.connections.update({currentNode:neighbors})
        return self.connectAllNodes(x + 1,y,counter + 1)

    def createBoard(self):
        """"
        should create the game board
        first create all the nodes 
        connect all the nodes
        """
        self.createAllNodes(self.allNodes,0,0,0)
        self.connectAllNodes(0,0,0)
def printBoard(board,rows):
    for x in range(len(board)):
        if (x % rows == 0):
            print("\n")
        print(board[x])

if __name__ == "__main__":
    first = Node(3,3)
    graph = Graph()
    graph.setTotalNodes()
    graph.createBoard()


