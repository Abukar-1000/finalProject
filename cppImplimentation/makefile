program: node.o main.o chessPiece.o
	g++ -g -std=c++11 node.o chessPiece.o main.o -o program 
node.0: node.cpp node.h
	g++ -c -std=c++11 node.cpp
chessPiece.o: chessPiece.cpp chessPiece.h
	g++ -c -std=c++11 chessPiece.cpp
main.o: main.cpp node.h
	g++ -c -std=c++11 main.cpp
run: program
	./program
clean: 
	del program
	del *.o
