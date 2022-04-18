#include <iostream>
#include "node.h"
#include "node.cpp"
#include <vector>
#include "chessPiece.h"
#include "chessPiece.cpp"

void printAllValues(Node<int>* head);
void addToEnd(Node<int>* first, Node<int>* item){
    Node<int>* head = first;
    while (head->getNextNode() != NULL){
        head = head->getNextNode();
    }
    
    // newNode.setX(4);
    // newNode->setY(0);
    // newNode->setDegree(6);
    Node<int>* previous = head;
    previous->setNextNode(item);
}

int main(){
    std::vector<Node<int>*> allNodes;
    Node<int> first(0,0,2);
    Node<int> second(1,0,4);
    Node<int> third(3,0,4);
    first.setNextNode(&second);
    second.setNextNode(&third);
    printAllValues(&first);
    Node<int> newNode(5,0,86);
    addToEnd(&first,&newNode);
    printAllValues(&first);
    allNodes.push_back(&first);
    allNodes.push_back(&second);
    allNodes.push_back(&third);
    allNodes.push_back(&newNode);
    for (auto i = allNodes.begin(); i != allNodes.end(); ++i){
        std::cout << *(i) << "\n";
        Node<int>* current = *i;
        std::cout << " (" << current->getX() << "," << current->getY() << ") " << current->getDegree() << "\n";
    }
    // first.setX(0);
    // first.setY(0);
    // first.setDegree(2);
    first.setOrderVisited(1);
    ChessPiece<int> firsts = ChessPiece<int>(&first,NULL);
    std::cout << "X: " << firsts.getCurrent()->getX() << " Y: " << firsts.getCurrent()->getY() << " degree:  " << firsts.getCurrent()->getDegree() << " orderVisited: " << firsts.getCurrent()->getOrderVisited() << "\n";
    std::cout << "og: " << &first << " second: " << firsts.getCurrent();
    return 0;
}

void printAllValues(Node<int>* first){
    Node<int>* head = first;
    while (head != NULL){
        std::cout << "X: " << head->getX() << " Y: " << head->getY() << " Degree: " << head->getDegree() << " \n";
        head = head->getNextNode();
    }
}

