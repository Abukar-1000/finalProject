#include "chessPiece.h"
#include "node.h"

template <typename T>
ChessPiece<T>::ChessPiece(){
    this->currentNode = NULL;
    this->neighbors = NULL;
}

template <typename T>
ChessPiece<T>::ChessPiece(Node<T>* current,Node<T>* neighbors){
    this->currentNode = current;
    this->neighbors = neighbors;
}

template <typename T>
void ChessPiece<T>::setCurrent(Node<T>* current){
    this->currentNode = current;
}

template <typename T>
void ChessPiece<T>::setNeighbors(Node<T>* neighbors){
    this->neighbors = neighbors;
}

template <typename T>
Node<T>* ChessPiece<T>::getCurrent(){
    return this->currentNode;
}

template <typename T>
Node<T>* ChessPiece<T>::getNeighbors(){
    return this->neighbors;
}