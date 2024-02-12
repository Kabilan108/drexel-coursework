#include<stdio.h>

//  Write a function initArr that takes an array of integers and its length as arguments; returns nothing; and initializes each element of the inputted array with the numbers 0; 1; …; up to the inputted length.

void initArr(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        *(arr + i) = i;
    }
}

// Write a function initStr that takes a string as an argument, returns nothing, and initializes each character of the inputted string with the letters a, b, …, up to the letter at the inputted length. You may assume the inputted string’s length is ≤ 26 characters.
void initStr(char str[], int n) {
    char l = 'a';
    for (int i = 0; i < n; i++) {
        str[i] = l + i;
        if (i > 24) {
            break;
        }
    }
}

int main() {
    int arr[10];
    char str[10];

    initArr(arr, 10);
    initStr(str, 10);

    printf("Array: ");
    for (int i = 0; i < 10; i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");

    printf("String: '%s'", str);
    printf("\n");
}
