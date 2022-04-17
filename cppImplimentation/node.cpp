#include <iostream>
#include "node.h"

template <typename T>
Node<T>::Node(){
    this->orderVisited = 0;
    this->visited = false;
    this->nextNode = NULL;
}

template <typename T>
Node<T>::Node(T x,T y,T degree){
    this->x = x;
    this->y = y;
    this->degree = degree;
    this->orderVisited = 0;
    this->visited = false;
    this->nextNode = NULL;
}

template <typename T>
void Node<T>::setX(T x){
    this->x = x;
}

template <typename T>
void Node<T>::setY(T y){
    this->y = y;
}

template <typename T>
void Node<T>::setDegree(T degree){
    this->degree = degree;
}

template <typename T>
void Node<T>::setOrderVisited(T order){
    this->orderVisited = order;
}

template <typename T>
void Node<T>::setIsVisited(bool visited){
    this->visited = visited;
}

template <typename T>
void Node<T>::setNextNode(Node* next){
    this->nextNode = next;
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
T Node<T>::getDegree(){
    return this->degree;
}

template <typename T>
T Node<T>::getOrderVisited(){
    return this->orderVisited;
}

template <typename T>
bool Node<T>::getVisited(){
    return this->visited;
}

template <typename T>
Node<T>* Node<T>::getNextNode(){
    return this->nextNode;
}