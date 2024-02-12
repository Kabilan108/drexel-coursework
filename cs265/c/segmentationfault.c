// segmentationfault.c

#include<stdio.h>

int main(int argc, char *argv[]) {
    int x = 5;
    int *p = &x;
    printf("%p, %d\n", p, *p);
    *p = 89; // this is fine
    printf("%d\n", *p);
    p = 77; // should be *p = 77
    printf("Foo\n");
    printf("%d\n", *p);
    printf("Bar\n");
}
