# Author: Tony K. Okeke
# Date:   03.13.2024

CC = gcc
CFLAGS = -Wall -Wextra -Werror

all: grades 

grades: grades.o ll.o mystring.o utils.o
	$(CC) $(CFLAGS) -o grades grades.o mystring.o ll.o utils.o

grades.o: grades.c ll.h mystring.h utils.h
	$(CC) $(CFLAGS) -c grades.c

ll.o: ll.c ll.h mystring.h
	$(CC) $(CFLAGS) -c ll.c mystring.h

utils.o: utils.c ll.h mystring.h utils.h
	$(CC) $(CFLAGS) -c utils.c

mystring.o: mystring.c mystring.h
	$(CC) $(CFLAGS) -c mystring.c

clean:
	rm -f grades grades.o mystring.o ll.o utils.o
