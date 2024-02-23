// Author: Tony K Okeke
// Date:   02-22-2024

#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

// desc: Print usage string
// return: 2 - exit code
int printUsage() {
    printf("Usage: myfgrep PATTERNS [FILE]\n");
    printf("Try 'myfgrep --help' for more information.\n");
    return 2;
}

// desc: Check if a line contains a pattern
// return: 1 - true, 0 - false
int strContains(const char *line, const char *pattern) {
    const char *p1;
    const char *p2;
    const char *p3;

    for (p1 = line; *p1 != '\0'; p1++) {
        p2 = p1;
        p3 = pattern;

        while (*p3 != '\0' && *p2 == *p3) {
            p2++;
            p3++;
        }

        if (*p3 == '\0') {
            return 1;
        }
    }

    return 0;
}

// desc: Process a file and return if pattern was found
// return: 1 - pattern found, 0 - pattern not found
int processFile(FILE *fp, const char *pattern) {
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    int found = 0;

    while ((read = getline(&line, &len, fp)) != -1) {
        if (strContains(line, pattern) == 1) {
            printf("%s", line);
            found = 1;
        }
    }

    free(line);
    return found;
}

int main(int argc, char *argv[]) {
    if (argc > 3 || argc == 1) {
        return printUsage();
    }

    const char *pattern = argv[1];
    FILE *fp;

    if (argc == 3) {
        fp = fopen(argv[2], "r");
        if (fp == NULL) {
            int error = errno;
            fprintf(stderr, "myfgrep: %s: ", argv[2]);
            switch (error) {
                case ENOENT:
                    fprintf(stderr, "No such file or directory\n");
                    break;
                case EACCES:
                    fprintf(stderr, "Permission denied\n");
                    break;
                default:
                    perror("");
                    break;
            }
            return 2;
        }
    } else {
        fp = stdin;
    }

    int found = processFile(fp, pattern);
    
    if (fp != stdin) {
        fclose(fp);
    }

    return found ? 0 : 1;
}
