program: node.o main.o
	g++ -g -std=c++11 node.o main.o -o program 
node.0: node.cpp node.h
	g++ -c -std=c++11 node.cpp
main.o: main.cpp node.h
	g++ -c -std=c++11 main.cpp
run: program
	./program
clean: 
	del program
	del *.o
