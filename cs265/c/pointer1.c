#include <stdio.h>

int main(int argc, char *argv[]) {
    int x = 5;
    int *p = &x;

    printf("pointer\tdereference\tvalue\n");

    printf("%p\t%d\t%d\n", p, *p, x);

    x = 200;
    printf("%p\t%d\t%d\n", p, *p, x);

    *p = 30;
    printf("%p\t%d\t%d\n", p, *p, x);
}
