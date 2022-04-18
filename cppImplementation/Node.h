#include <iostream>
#ifndef NODE_H_EXISTS
#define NODE_H_EXISTS

template <typename T>
class Node{
    private:
        T x;
        T y;
        T degree;
        T orderVisited;
        bool visited;
        Node* nextNode;
    public:
        Node();
        Node(T x,T y,T degree,T orderVisited);
        void setX(T x);
        void setY(T y);
        void setDegree(T degree);
        void setOrderVisited(T order);
        void setNext(Node next);
        T getX();
        T getY();
        T getDegree();
        T getOrderVisited();
        Node* getNext();
};

#endif