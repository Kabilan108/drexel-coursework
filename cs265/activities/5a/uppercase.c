
#include<stdio.h>

void uppercase(char str[]) {
    int c;
    while (*str != '\0') {
        c = (int) *str;
        if (c >= 97 && c <= 122) {
            *str = (char) c - 32;
        }
        str++;
    }
}


int main() {
    char str1[] = "this is in LOWERcase";
    printf("original: %s\n", str1);
    uppercase(str1);
    printf("updated:  %s\n\n", str1);

    char str2[] = "this is in LOWERcase wITh nuMBERS 124 and symbols **==__%";
    printf("original: %s\n", str2);
    uppercase(str2);
    printf("updated:  %s\n\n", str2);

    char str3[] = "abcdefghijklmnopqrstuvwxyz1234567890-=_+][]()*&^%^$#!";
    printf("original: %s\n", str3);
    uppercase(str3);
    printf("updated:  %s\n\n", str3);
}
