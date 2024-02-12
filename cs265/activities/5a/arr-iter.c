
#include<stdio.h>

int main() {
    int arr[] = {0, 1,2,3,4,5,6,7,8,9};
    int n = 10;

    for (int i = 0; i < n; i++) {
        printf("%d\n", *(arr + i));
    }
}
