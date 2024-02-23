#include <stdio.h>

void weirdSwapPtrs(char *s1, char *s2) {
    char *end1 = s1;
    char *end2 = s2;
    char temp;

    // move pointers to the last character in each string
    while (*end1) ++end1;
    while (*end2) ++end2;
    --end1;
    --end2;

    // swap characters
    while (s1 <= end1 && s2 <= end2) {
        temp = *end1;
        *end1 = *end2;
        *end2 = temp;
        --end1;
        --end2;
        ++s1;
        ++s2;
    }
}

int main(int argc, char* argv[]) {
    char x[] = "abc";
    char y[] = "defghi";

    printf("original:\n");
    printf("x = '%s'\n", x);
    printf("y = '%s'\n", y);

    weirdSwapPtrs(x, y);

    printf("swapped:\n");
    printf("x = '%s'\n", x);
    printf("y = '%s'\n", y);



    char p[] = "defghi";
    char q[] = "jkl";

    printf("original:\n");
    printf("p = '%s'\n", p);
    printf("q = '%s'\n", q);

    weirdSwapPtrs(p, q);

    printf("swapped:\n");
    printf("p = '%s'\n", p);
    printf("q = '%s'\n", q);
}

