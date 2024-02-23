
#include <stdio.h>

int * initArr(int n) {
    int x[n];
    for (int i = 0; i < n; i++) {
        x[i] = i;
    }
    return x;
} 

int main() {
    int n = 5;
    int *x = initArr(n);
    for (int i = 0; i < n; i++) {
        printf("%d\n", *(x + i));
    }
}
