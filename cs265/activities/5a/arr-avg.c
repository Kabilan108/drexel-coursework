#include<stdio.h>

// Write a function avgArr that takes an array of integers and its length as arguments and returns the average of the array.
float avgArr(int *arr, int n) {
    int sum = 0;

    for (int i = 0; i < n; i++) {
        sum = sum + *(arr + i);
    }
    
    return sum/n;
}

int main() {
    int x[] =  {1, 2, 3, 4, 5};
    float avg = avgArr(x, 5);

    printf("%f\n", avg);
}
