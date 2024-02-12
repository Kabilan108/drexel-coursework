#include<stdio.h>
#include<stdbool.h>
#include<string.h>

bool equalArr(int *x, int *y, int m, int n) {
    // *x, m -> array 1
    // *y, n -> array 2

    if (m != n) {
        return false;
    }

    for (int i = 0; i < n; i++) {
        if (x[i] != y[i]) {
            return false;
        }
    }

    return true;
}

bool equalStr(char x[], char y[]) {
    while (*x == *y) {
        if (*x == '\0') {
            return true;
        }
        x++;
        y++;
    }
    return false;
}

int main() {
    bool isEqual;

    int x[] = {1, 2, 3, 4, 5};
    int y[] = {1, 2, 3, 4, 5};
    int z[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    isEqual = equalArr(x, y, 5, 5);
    printf("isEqual(x,y): %d\n", isEqual);

    isEqual = equalArr(z, y, 5, 9);
    printf("isEqual(z,y): %d\n", isEqual);
    
    char p[] = "This is a string";
    char q[] = "This is a string";
    char r[] = "This is a long string";

    isEqual = equalStr(p, q);
    printf("isEqual(p,q): %d\n", isEqual);

    isEqual = equalStr(r, q);
    printf("isEqual(r,q): %d\n", isEqual);
}
