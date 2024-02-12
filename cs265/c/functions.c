// functions.c

#include <stdio.h>

int add(int x, int y) {
    return x + y;
}

void printStuff(char *myStr) {
    printf("The string is: %s \n", myStr);
}

int main(int argc, char *argv[]) {
    int x = add(2, 3);

    printf("%d\n", x);
    printf("%d\n", add(2, 3));

    printStuff("abc");
    printStuff("hello world");
}
