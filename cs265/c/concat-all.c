#include <stdio.h>

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

int main() {
    char* x1 = "abc";
    char* x2 = "defghi";
    char* x3 = "z";
    char* xs[] = {x1, x2, x3};

    int n = sizeof(xs) / sizeof(char*);
    char dest[11];
    concatAll(xs, n, dest);

    printf("'%s' + '%s' + '%s' = '%s'\n", x1, x2, x3, dest);
}

