#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

int mystrlen(char* str) {
    int len = 0;
    while (str[len] != '\0') len++;
    return len;
}

char* concatAllHeap(char* xs[], int n) {
    int len = 1;
    for (int i = 0; i < n; i++) {
        len += mystrlen(xs[i]);
    }

    char* res = (char*) malloc(len * sizeof(char));
    if (res == NULL) return NULL;

    char* pos = res;
    for (int i = 0; i < n; i++) {
        char* p = xs[i];
        while (*p) {
            *pos++ = *p++;
        }
    }
    *pos = '\0';

    return res;
}

int main() {
    char* x1 = "abc";
    char* x2 = "defghi";
    char* x3 = "z";
    char* xs[] = {x1, x2, x3};

    int n = sizeof(xs) / sizeof(char*);
    char* res = concatAllHeap(xs, n);

    printf("'%s' + '%s' + '%s' = '%s'\n", x1, x2, x3, res);
}

