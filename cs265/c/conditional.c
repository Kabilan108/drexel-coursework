// conditional.c

#include <stdio.h>

int main (int argc, char *argv[]) {
    int x = 1;

    if (x == 1) {
        printf("x is 1\n");
    } else if (x == 2) {
        printf("x is 2\n");
    } else {
        printf("x is something else\n");
    }

    for (int i = 0; i < 5; i++) {
        printf("%d\n", i);
    }

    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }
}
