# Author: Tony K. Okeke
# Date:   03.13.2024

all: grades

grades: grades.o mystring.o ll.o
	gcc -o grades grades.o mystring.o ll.o

grades.o: grades.c mystring.h ll.h
	gcc -c grades.c

mystring.o: mystring.c mystring.h
	gcc -c mystring.c

ll.o: ll.c ll.h
	gcc -c ll.c

clean:
	rm -f grades grades.o mystring.o ll.o
