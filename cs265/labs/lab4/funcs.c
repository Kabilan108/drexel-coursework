// Lab 4
// Author: Tony K. Okeke
// Date:   02-12-2024

#include <stdio.h>

int find(int *arr, int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

void flipcase(char *str) {
   int c;
   while (*str != '\0') {
        c = (int) *str;
        if (c >= 97 && c <= 122) {
            *str = (char) c - 32;
        } else if (c >= 65 && c <= 90) {
            *str = (char) c + 32;
        }
        str++;
   }
}

void int2str(int n, char *s) {
    if (n == 0) {
        s[0] = '0';
        s[1] = '\0';
    } else {
        int i, j;
        char c;

        i = 0;
        while (n != 0) {
            s[i] = '0' + (n % 10);
            n = n / 10;
            i++;
        }

        for (j = 0; j < i/2; j++) {
            c = s[j];
            s[j] = s[i-j-1];
            s[i-j-1] = c;
        }

        s[i] = '\0';
    }
}

void mystrcat(char *p, char *q) {
    while (*p != '\0') {
        p++;
    }
    while (*q != '\0') {
        *p = *q;
        p++;
        q++;
    }
    *p = '\0';
}

