
#include<stdio.h>

void printpointer(int *ptr) {
}

int main(int argc, char *argv[]) {
    int x = 5;
    int *p = &x;
    printf("%p stores %p which contains %d\n", &p, p, *p);

    *p = 10;
    printf("%p stores %p which contains %d\n", &p, p, *p);

    int **q = &p;
    printf("%p stores %p which stores %p which contains %d\n", &q, q, *q, **q);

    **q = 0;
    printf("%p stores %p which stores %p which contains %d\n", &q, q, *q, **q);

    int y = 69;
    *q = &y;
    printf("%p stores %p which stores %p which contains %d\n", &q, q, *q, **q);
}
