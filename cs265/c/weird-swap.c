#include <stdio.h>

int mystrlen(char* str) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

void weirdSwap(char* x, char* y) {
    // get string lengths
    int len_x = mystrlen(x);
    int len_y = mystrlen(y);
    int swap_len = len_y < len_x ? len_y : len_x;

    // allocate temp vars
    char temp_x[swap_len + 1];
    char temp_y[swap_len + 1];

    // copy last swap_len characters from x & y to temp_y & temp_x
    for (int i = 0; i < swap_len; i++) {
        temp_y[i] = x[len_x - 1 - i];
        temp_x[i] = y[len_y - 1 - i];
    }

    // replace beginning of swap_len with temp_[xy]
    for (int i = 0; i < swap_len; i++) {
        x[i] = temp_x[i];
        y[i] = temp_y[i];
    }

    x[len_x] = '\0';
    y[len_y] = '\0';
}

int main(int argc, char* argv[]) {
    char x[] = "abc";
    char y[] = "defghi";

    printf("original:\n");
    printf("x = '%s'\n", x);
    printf("y = '%s'\n", y);

    weirdSwap(x, y);

    printf("swapped:\n");
    printf("x = '%s'\n", x);
    printf("y = '%s'\n", y);



    char p[] = "defghi";
    char q[] = "jkl";

    printf("original:\n");
    printf("p = '%s'\n", p);
    printf("q = '%s'\n", q);

    weirdSwap(p, q);

    printf("swapped:\n");
    printf("p = '%s'\n", p);
    printf("q = '%s'\n", q);
}
