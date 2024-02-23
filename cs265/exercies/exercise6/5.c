
#include <stdio.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++) {
        char *arg = argv[i];
        if (arg[0] == 'a' && arg[1] == 'b' && arg[2] == 'c' && arg[3] == '\0') {
            printf("abc found\n");
            return 0;
        }
    }
    
    printf("abc NOT found\n");
    return 0;
}
