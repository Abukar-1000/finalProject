#include "board.h"

Board::Board(){
    this->totalNodes = 64;
}

Board::Board(int total){
    this->totalNodes = total;
}

Board::~Board(){
    // does nothing for now
}
void Board::setTotalNodes(int total){
    this->totalNodes = total;
}

void Board::createAllNodes(std::vector<Node<int>*> totalNodes,int x,int y,int counter){
    // pass
}
