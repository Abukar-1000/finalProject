#include <iostream>
#include "Node.h"
int main(){
    Node<int> first;
    first.setX(0);
    first.setY(0);
    float i = 10.5;
    float* addresss = &i + 2;
    std::cout << first.getX() << " " << first.getY() << std::endl;
    return 0;
}