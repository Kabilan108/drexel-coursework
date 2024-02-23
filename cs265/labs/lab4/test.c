#include <stdio.h>
#include <string.h>
#include "funcs.c"

void printArray(int array[], int length) {
    printf("[");
    for(int i = 0; i < length; i++) {
        printf("%d", array[i]);
        if(i < length - 1) printf(", ");
    }
    printf("]\n");
}

void test_find() {
    printf("Testing `find`\n");

    int array1[] = {1, 2, 3, 4, 5};
    int len1 = 5;
    printf("Existing element (3) -> Expected: 2, Got: %d\n", find(array1, len1, 3));

    int array2[] = {1, 2, 3, 4, 5};
    int len2 = 5;
    printf("Non-existing element (6) -> Expected: -1, Got: %d\n", find(array2, len2, 6));

    int array3[] = {};
    int len3 = sizeof(array3) / sizeof(array3[0]);
    printf("Empty array -> Expected: -1, Got: %d\n", find(array3, len3, 3));

    printf("\n");
}

void test_flipcase() {
    printf("Testing `flipcase`\n");

    char str1[] = "abcX y-Z";
    printf("'%s' --> ", str1);
    flipcase(str1);
    printf("'%s'\n", str1);

    char str2[] = "12345!@#$";
    printf("'%s' --> ", str2);
    flipcase(str2);
    printf("'%s'\n", str2);

    char str3[] = "";
    printf("'%s' --> ", str3);
    flipcase(str3);
    printf("'%s'\n", str3);
    
    char str4[] = "ABCXYZ123abcxyz";
    printf("'%s' --> ", str4);
    flipcase(str4);
    printf("'%s'\n", str4);

    printf("\n");
}

void test_int2str() {
    printf("Testing `int2str`\n");

    int n = 327;
    char s[4]; 
    int2str(n, s);
    printf("%d --> '%s'\n", n, s);

    n = 0;
    char t[2]; 
    int2str(n, t);
    printf("%d --> '%s'\n", n, t);

    n = 12214;
    char v[6]; 
    int2str(n, v);
    printf("%d --> '%s'\n", n, v);

    n = 5;
    char w[2]; 
    int2str(n, w);
    printf("%d --> '%s'\n", n, w);

    printf("\n");
}

int test_mystrcat() {
    printf("Testing `mystrcat`\n");

    char p[7] = "abc";
    char q[] = "de";
    printf("'%s' + '%s' --> ", p, q);
    mystrcat(p, q);
    printf("'%s'\n", p);

    char r[7] = "uv";
    char s[] = "xyz";
    printf("'%s' + '%s' --> ", r, s);
    mystrcat(r, s);
    printf("'%s'\n", r);

    printf("\n");
}

int main() {
    test_find();
    test_flipcase();
    test_int2str();
    test_mystrcat();
}

