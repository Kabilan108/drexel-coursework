
#include <stdio.h>

int main() {
    int x[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    int n = 9;

    for (int i = 0; i < n; i++) {
        printf("x[%d] is stored at %p and contains %d\n", i, x+i, *(x+i));
    }
}
