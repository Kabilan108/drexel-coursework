
#include <stdio.h>
#include <stdlib.h>

int sumIntPtr(int *arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum = sum + *arr[i];
    }
    return sum;
}

int main() {
    int *arr[5];

    for (int i = 0; i < 5; i++) {
        arr[i] = (int *) malloc(sizeof(int));
        if (arr[i] == NULL) {
            return 1;
        }
        *arr[i] = i * 10;
    }

    for (int i = 0; i < 5; i++) {
        printf("arr[%d] points to %d\n", i, *arr[i]);
    }

    int sum = sumIntPtr(arr, 5);
    printf("their sum is %d\n", sum);
}
