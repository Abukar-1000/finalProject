#include <iostream>

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

template <typename T>
Node<T>::Node(){
    this->x = 0;
    this->y = 0;
    this->degree = 0;
    this->orderVisited = 0;
    this->visited = false;
    this->nextNode = NULL;
}

template <typename T>
Node<T>::Node(T x,T y,T degree,T orderVisited){
    this->x = x;
    this->y = y;
    this->degree = degree;
    this->orderVisited = orderVisited;
    this->visited = false;
    this->nextNode = NULL;
}

template <typename T>
T Node<T>::getX(){
    return this->x;
}

template <typename T>
T Node<T>::getY(){
    return this->y;
}

template <typename T>
void Node<T>::setNext(Node next){
    this->nextNode = &next;
}

template <typename T>
Node<T>* Node<T>::getNext(){
    return this->nextNode;
}

int main(){
    Node<int> first(0,0,0,0);
    Node<int> second(1,0,0,0);
    first.setNext(second);
    std::cout << first.getX() << std::endl;
    std::cout << first.getNext()->getX() <<std::endl;
    return 0;
}