#include <vector>
#include "node.h"
#include "chessPiece.h"

#ifndef BOARD_H_EXISTS
#define BOARD_H_EXISTS

class Board{
    private:
        std::vector<Node<int>*> allNodes;
        ChessPiece<int>* board;
        int totalNodes;
    public:
        Board();
        Board(int totalNodes);
        ~Board();
        void setTotalNodes(int total);
        void createAllNodes(std::vector<Node<int>*> totalNodes,int x,int y,int counter);
        Node<int>* findNode(int index,int x,int y,Node<int>* node);
        std::vector<Node<int>*> findNeighbors(int originalX,int originalY,int index,std::vector<Node<int>*> neighbors);
        void connectAllNodes(int x,int y,int counter);
        void createBoard();
        void printBoard();
        void updateDegree(Node<int>* node);
        Node<int>* findLeastDegree(Node<int>* node);
        void makeTour(Node<int>* startNode);
        void test();
};
#endif