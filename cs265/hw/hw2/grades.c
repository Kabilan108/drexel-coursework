// Author: Tony K. Okeke
// Date:   03.13.2024

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

#include "ll.h"
#include "mystring.h"

int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s FILEPATH\n", argv[0]);
        return 1;
    }

    int len = mystrlen(argv[1]);
    printf("Length of string: %d\n", len);
}
