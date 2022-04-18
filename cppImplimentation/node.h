#include <iostream>
#ifndef NODE_H_EXISTS
#define NODE_H_EXISTS

template <typename T>
class Node {
    private:
        T x;
        T y;
        T degree;
        T orderVisited;
        bool visited;
        Node<T>* neighbors;
        Node<T>* nextNode; 
    public:
        Node();
        Node(T x,T y,T degree);
        void setX(T x);
        void setY(T y);
        void setDegree(T degree);
        void setOrderVisited(T order);
        void setIsVisited(bool visited);
        void setNextNode(Node<T>* next);

        T getX();
        T getY();
        T getDegree();
        T getOrderVisited();
        bool getVisited();
        Node<T>* getNextNode();
};
 
#endif