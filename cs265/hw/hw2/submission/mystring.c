// Author: Tony K. Okeke
// Date:   03.13.2024

#include "mystring.h"

// compute the length of a string
int mystrlen(const char* str) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

// compare two strings
int mystrcmp(const char* str1, const char* str2) {
    while (*str1 == *str2) {
        if (*str1 == '\0') {
            return 0;
        }
        str1++;
        str2++;
    }
    return *str1 - *str2;
}

// compare two strings up to n characters
int mystrncmp(const char* str1, const char* str2, int n) {
    while (n > 0) {
        if (*str1 != *str2) {
            return *str1 - *str2;
        }
        if (*str1 == '\0') {
            return 0;
        }
        str1++;
        str2++;
        n--;
    }
    return 0;
}

// copy a string to another string up to n characters
char* mystrncpy(char* dest, const char* src, int n) {
    char* originalDest = dest;
    while (*src != '\0' && n > 0) {
        *dest++ = *src++;
        n--;
    }
    while (n > 0) {
        *dest++ = '\0';
        n--;
    }
    return originalDest;
}

// concatenate src to dest up to n characters
char* mystrncat(char* dest, const char* src, int n) {
    char* originalDest = dest;
    while (*dest != '\0') {
        dest++;
    }
    while (*src != '\0' && n > 0) {
        *dest++ = *src++;
        n--;
    }
    *dest = '\0';
    return originalDest;
}
