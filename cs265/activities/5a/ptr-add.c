
#include<stdio.h>

void foo(int *p) {
    *p = *p + 1;
}

int main() {
    int x = 5;
    foo(&x);
    printf("x = %d\n", x);
}
