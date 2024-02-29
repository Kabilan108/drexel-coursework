#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Match {
    int lineNum;
};

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s PATTERN\n", argv[0]);
        return 1;
    }

    ssize_t read;
    size_t len = 0;
    char* line = NULL;
    int count = 0, currentLine = 0;

    struct Match* matches = NULL;

    while ((read = getline(&line, &len, stdin)) != -1) {
        currentLine++;

        if (line[read - 1] == '\n') {
            line[read - 1] = '\0';
            read--;
        }

        if (strcmp(line, argv[1]) == 0) {
            struct Match* temp = realloc(matches, (count + 1) * sizeof(struct Match));
            if (temp == NULL) {
                free(matches);
                fprintf(stderr, "Failed to allocate memory\n");
                return 1;
            }

            matches = temp;
            matches[count].lineNum = currentLine;
            count++;
        }
    }

    if (count == 0) {
        printf("No matches found\n");
    } else {
        printf("Here are all matches:\n");
        for (int i = 0; i < count; i++) {
            printf("%d\n", matches[i].lineNum);
        }
    }

    free(matches);
    free(line);
    return 0;
}

