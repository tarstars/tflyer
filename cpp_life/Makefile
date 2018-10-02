driver: main.o life_field.o field_util.o
	g++ main.o life_field.o field_util.o -o driver -Wall

main.o: main.cpp
	g++ -c main.cpp -o main.o -Wall

life_field.o: life_field.cpp matrix.h
	g++ -c life_field.cpp -o life_field.o -Wall

field_util.o: field_util.cpp life_field.h matrix.h
	g++ -c field_util.cpp -o field_util.o -Wall

clean:
	rm driver *.o
