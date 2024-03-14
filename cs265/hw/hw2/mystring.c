// Author: Tony K. Okeke
// Date:   03.13.2024

#include "mystring.h"

// compute string length
int mystrlen(char* str) {
    int len = 0;
    while (str[len] != '\0') len++;
    return len;
}
