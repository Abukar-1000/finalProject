#include <iostream>
#include "node.h"

int main(){
    Node<int> first = Node<int>();
    first.setX(0);
    first.setY(0);
    first.setDegree(2);
    first.setOrderVisited(1);
    std::cout << "X: " << first.getX() << "Y: " << first.getY() << " degree:  " << first.getDegree() << first.getDegree() << " orderVisited: " << first.getOrderVisited();
    return 0;
}