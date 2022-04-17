#include <iostream>
#include "node.h"
#include "node.cpp"
#include "chessPiece.h"
#include "chessPiece.cpp"

int main(){
    Node<int> first(0,0,2);
    // first.setX(0);
    // first.setY(0);
    // first.setDegree(2);
    first.setOrderVisited(1);
    ChessPiece<int> firsts = ChessPiece<int>(&first,NULL);
    std::cout << "X: " << firsts.getCurrent()->getX() << " Y: " << firsts.getCurrent()->getY() << " degree:  " << firsts.getCurrent()->getDegree() << " orderVisited: " << firsts.getCurrent()->getOrderVisited();
    return 0;
}