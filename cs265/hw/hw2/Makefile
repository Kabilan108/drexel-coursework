# Author: Tony K. Okeke
# Date:   03.13.2024

all: grades test-ll

grades: grades.o mystring.o ll.o
	gcc -o grades grades.o mystring.o ll.o

test-ll: test-ll.o ll.o mystring.o
	gcc -o test-ll test-ll.o ll.o mystring.o

grades.o: grades.c mystring.h ll.h
	gcc -c grades.c

test-ll.o: test-ll.c ll.h
	gcc -c test-ll.c

mystring.o: mystring.c mystring.h
	gcc -c mystring.c

ll.o: ll.c ll.h
	gcc -c ll.c

clean:
	rm -f grades grades.o mystring.o ll.o test-ll test-ll.o
