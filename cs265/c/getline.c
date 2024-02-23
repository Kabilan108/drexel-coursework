#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    char *s = NULL;
    size_t nbytes = 0;
    ssize_t nchar;

    // if you pass a null pointer and 0 bytes to getline
    // it'll call malloc to allocate enough space for the string the user types
    // it will be stored inside the pointer we pass it
    nchar = getline(&s, &nbytes, stdin);
    
    // if OOM, malloc returns null
    if (s == NULL) exit(1);
    
    // getline returns -1 if EOF received
    if (nchar == -1) return 0;
    s[nchar -1] = '\0';  //  replace newline with null char
    
    printf("%ld, %lu, %p, '%s'\n", nchar, nbytes, s, s);
    free(s);
}
