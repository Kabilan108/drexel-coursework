
#include<stdio.h>

// Write a function inc that takes an integer as an argument and returns the integer plus one.
int inc(int x) {
    return x + 1;
}

// Write a function named incPtr that takes an integer pointer as an argument, returns nothing, and increments the integer pointed to by the inputted pointer.
int incPtr(int *p) {
    *p = *p + 1;
}

int main() {
    int x = 10;

    printf("%d\n", x);

    x = inc(x);
    printf("%d\n", x);

    incPtr(&x);
    printf("%d\n", x);
}

