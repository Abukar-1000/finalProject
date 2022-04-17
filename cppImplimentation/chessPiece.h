#ifndef CHESSPIECE_H_EXISTS
#define CHESSPIECE_H_EXISTS
#include "node.h"

template <typename T>
class ChessPiece{
    private:
        Node<T>* currentNode;
        Node<T>* neighbors;
    public:
        ChessPiece();
        ChessPiece(Node<T>* current,Node<T>* neighbors);
        void setCurrent(Node<T>* current);
        void setNeighbors(Node<T>* neighbors);
        Node<T>* getCurrent();
        Node<T>* getNeighbors();        
};
#endif