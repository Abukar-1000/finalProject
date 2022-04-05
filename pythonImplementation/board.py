from platform import node
from node import *

""""
was changed again
create the hueristic value of each piece
update the values after each turn ?
mark vistied nodes 

"""
class Graph(object):

    def __init__(self,dimension = "8x8"):
        self.dimension = dimension
        self.totalNodes = 0
        self.connections = dict(())

    def setTotalNodes(self):
        allValues = [int(x) for x in self.dimension.split("x")]
        self.totalNodes = allValues[0] * allValues[1]
    def createBoard(self,x,y,counter):
        
        if (counter == self.totalNodes):
            return 1
        elif (x > 7):
            x = 0
            print("\n",end="")
            return self.createBoard(x,y + 1,counter)
        else:
            newNode = Node(x,y)
            self.connections.update({newNode:[]})
            print(f"({newNode.x},{newNode.y})",end=" ")
            return self.createBoard(x + 1,y,counter + 1)
    def findNeighbors(self,Node,index = 0,answers = []):
        xOffsets = (1,-1,1,-1,2,-2,2,-2)
        yOffsets = (2,2,-2,-2,1,1,-1,-1)
        if (index == (len(xOffsets))):
            return answers
        else:
            newX = Node.x + xOffsets[index]
            newY = Node.y + yOffsets[index]
            if (((newX >= 0) and (newX <= 7)) and ((newY >= 0) and (newY <= 7))):
                answers.append((newX,newY))
        return self.findNeighbors(Node,index+1,answers)
        
    def createAllNodes(self,x,y):
        """"
        base if y > 7
        print new lane if x > 7
        increment the x and y 

        create a new node 
        set its x and y values 
        find all valid neighbors for each node 
        
        """
        if (y > 7):
            return 1
        elif (x > 7):
            x = 0
            print("\n",end="")
            return self.createAllNodes(x,y + 1)
        else:
            newNode = Node(x,y)
            if (newNode not in self.connections):
                neighbors = self.findNeighbors(newNode,0,[])
                self.connections.update({newNode:neighbors})
                newNode.degree = len(neighbors)
            # else:
            #     neighbors = self.findNeighbors(newNode,0,[])
            #     self.connections[newNode].extend(neighbors)
            #     newNode.degree = len(neighbors)
            print(f"({newNode.degree})",end=" ")
            return self.createAllNodes(x + 1,y)

def printBoard(board,rows):
    for x in range(len(board)):
        if (x % rows == 0):
            print("\n")
        print(board[x])

if __name__ == "__main__":
    # xStart,yStart = (5,5)
    # board = [[0 for x in range(xStart)] for y in range(yStart)]
    # board[0][1] = "k"
    # printBoard(board,yStart)
    # print(board)
    first = Node(3,3)
    graph = Graph()
    # graph.setTotalNodes()
    # print(graph.totalNodes)
    # answers = graph.findNeighbors(first,0,[])
    # for x in answers:
    #     print(x)
    # graph.createAllNodes(0,0)
    # print(graph.connections)
    graph.setTotalNodes()
    graph.createBoard(0,0,0)
    print(graph.connections)
    print(graph.totalNodes)
