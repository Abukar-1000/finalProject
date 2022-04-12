from node import *
""""
create all nodes 
link all nodes 

algorithm:
create the hueristic value of each piece (degree attribute)
update the values after each turn 
mark vistied nodes 
always choose the node with the least degree

selecting:
get the degree of neighbors | check if a neighbor has been visited 
select the neighbor with the least degree
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
            return self.createAllNodes(totalNodes,x + 1,y,counter + 1)
    def findNode(self,index,x,y,node = None):
        """"
        should find a node with the given x,y values 
        so i can find already existing nodes with the given (x,y)
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
                    newNode = self.findNode(0,newX,newY,Node(-1,-1))
                    totalNodes.append(newNode)
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
            currentNode = self.findNode(0,x,y,Node(-1,-1))
            neighbors = self.findNeighbors(currentNode.x,currentNode.y,0,[])
            currentNode.degree = len(neighbors)
            self.connections.update({currentNode:neighbors})
        return self.connectAllNodes(x + 1,y,counter + 1)

    def createBoard(self):
        """"
        should create the game board
        first create all the nodes 
        connect all the nodes
        """
        self.setTotalNodes()
        self.allNodes = self.createAllNodes([],0,0,0)
        self.connectAllNodes(0,0,0)

    def printBoard(self):
        """"
        print the nodes at each position of the gamboard 
        """
        counter = 0
        for node in self.allNodes:
            if (counter % 8 == 0):
                print("\n",end="")
            if (node.orderVisited >= 0):
                print(node.orderVisited,end=" ")
            else:
                print(f"({node.x},{node.y})",end=" ")
            counter += 1
    def updateDegree(self,node):
        """"
        from a given node | should update its degree
        find node & get neighbors
        check if neighbor has been visited | if so don't increment degree
        increment degree
        set new degree
        """
        degree = 0
        # for nodes in self.allNodes:
        #     if ((nodes.x == node.x) and (nodes.y == node.y)):
        #         print(f"incoming {node} | actual: {nodes}")
        # print(self.connections[node])
        neighbors = self.connections[node]
        for neighbor in neighbors:
            if (neighbor.visited == False):
                degree += 1
        node.degree = degree

    def findLeastDigree(self,node):
        """""
        finds the neighbor with the least amount of moves available 
        """
        minimum = 10
        result = None
        neighbors = self.connections[node]
        for node in neighbors:
            self.updateDegree(node)
            if ((node.degree <= minimum) and (node.visited == False)):
                minimum = node.degree
                result = node
        return result

    def makeTour(self,startSpot):
        """"
        given a starting node | should traverse the board and tour
        """
        path = None
        counter = 1
        path = startSpot
        currentSpot = startSpot
        for x in range(self.totalNodes):
            currentSpot.orderVisited = counter
            currentSpot.visited = True
            self.updateDegree(currentSpot)
            nextMove = self.findLeastDigree(currentSpot)
            currentSpot = nextMove
            path.nextNode = currentSpot
            counter += 1
        return path

    def test(self):
        spot = input("(x,y):    ")
        values = [int(x) for x in spot.split(',')]
        x = values[0]
        y = values[1]
        startNode = self.findNode(0,x,y,Node(-1,-1))
        print(f"({startNode.x},{startNode.y}) address: {startNode} | {self.allNodes[0]}")
        path = self.makeTour(startNode)
        print("starting tour:")
        counter = 0
        while (path.nextNode != None):
            print(f"({counter}): ({path.x},{path.y})")
        self.printBoard()

if __name__ == "__main__":
    first = Node(3,3)
    graph = Graph()
    # graph.setTotalNodes()
    graph.createBoard()
    graph.test()
    # graph.breakTie(first)