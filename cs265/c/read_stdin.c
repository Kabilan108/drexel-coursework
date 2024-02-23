#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
    char** strings = NULL;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    int count = 0;

    // read stdin
    while ((read = getline(&line, &len, stdin)) != -1) {
        strings = realloc(strings, (count + 1) * sizeof(char*));
        if (strings == NULL) {
            exit(1);
        }

        strings[count] = malloc(read + 1);
        if (strings[count] == NULL) {
            exit(1);
        }

        strncpy(strings[count], line, read + 1);
        count++;
    }
    free(line);

    for (int i = 0; i < count; i++) {
        printf("%s", strings[i]);
        free(strings[i]);
    }

    free(strings);
    return 0;
}
