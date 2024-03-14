# Author: Tony K. Okeke
# Date:   03.13.2024

all: grades

grades: grades.o mystring.o
	gcc -o grades grades.o mystring.o

grades.o: grades.c mystring.h
	gcc -c grades.c

mystring.o: strfns.c strfns.h
	gcc -c mystring.c

clean:
	rm -f grades grades.o mystring.o
