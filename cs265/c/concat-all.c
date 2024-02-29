#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

int mystrlen(char* str) {
    int len = 0;
    while (str[len] != '\0') len++;
    return len;
}

void concatAll(char* xs[], int n, char* dest) {
    for (int i = 0; i < n; i++) {
        char* p = xs[i];
        while (*p != '\0') {
            *dest = *p;
            dest++;
            p++;
        }
    }
    *dest = '\0';
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

    char* p = "Solid";
    char* q = "Gold";
    char* r = "Magi";
    char* s = "karp";
    char* t[] = {p, q, r, s};

    int n_1 = sizeof(xs) / sizeof(char*);
    int n_2 = sizeof(t) / sizeof(char*);

    printf("# Testing `concatAll`:\n");
    char dest_1[11], dest_2[18];
    concatAll(xs, n_1, dest_1);
    concatAll(t, n_2, dest_2);
    printf(" - '%s' + '%s' + '%s' = '%s'\n", x1, x2, x3, dest_1);
    printf(" - '%s' + '%s' + '%s' + '%s' = '%s'\n", p, q, r, s, dest_2);


    printf("# Testing `concatAllHeap`:\n");
    char* res_1 = concatAllHeap(xs, n_1);
    char* res_2 = concatAllHeap(t, n_2);
    printf(" - '%s' + '%s' + '%s' = '%s'\n", x1, x2, x3, res_1);
    printf(" - '%s' + '%s' + '%s' + '%s' = '%s'\n", p, q, r, s, res_2);
}

