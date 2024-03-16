// Author: Tony K. Okeke
// Date:   03.13.2024

#ifndef MYSTRING_H
#define MYSTRING_H
    int mystrlen(const char* str);
    int mystrcmp(const char* str1, const char* str2);
    int mystrncmp(const char* str1, const char* str2, int n);

    char* mystrncpy(char* dest, const char* src, int n);
    char* mystrncat(char* dest, const char* src, int n);
#endif
