#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Pet {
    char name[16];
    int age;
    char species[16];
};

int main(int argc, char* argv[]) {
    ssize_t read;
    size_t len = 0;
    char* line = NULL;
    int count = 0;
    int capacity = 1; // Initial capacity for one pet

    struct Pet* pets = malloc(sizeof(struct Pet) * capacity);
    if (pets == NULL) {
        fprintf(stderr, "Failed to allocate memory\n");
        return 1;
    }

    while ((read = getline(&line, &len, stdin)) != -1) {
        // Resize the array if necessary
        if (count >= capacity) {
            capacity *= 2;
            struct Pet* temp = realloc(pets, sizeof(struct Pet) * capacity);
            if (temp == NULL) {
                fprintf(stderr, "Failed to reallocate memory\n");
                free(pets);
                return 1;
            }
            pets = temp;
        }

        // Read pet name
        if (read > 0 && read < 16) {
            // Store value, remove newlines
            strcpy(pets[count].name, line);
            pets[count].name[strcspn(pets[count].name, "\n")] = '\0';
        } else {
            fprintf(stderr, "Invalid input format\n");
            free(pets);
            return 1;
        }

        // Read pet age
        if (getline(&line, &len, stdin) != -1) {
            pets[count].age = atoi(line);
        } else {
            fprintf(stderr, "Invalid input format\n");
            free(pets);
            return 1;
        }

        // Read pet species
        if (getline(&line, &len, stdin) != -1 && read < 16) {
            // Store value, remove newlines
            strcpy(pets[count].species, line);
            pets[count].species[strcspn(pets[count].species, "\n")] = 0;
        } else {
            fprintf(stderr, "Invalid input format\n");
            free(pets);
            return 1;
        }

        count++;
    }

    // Print all pets
    for (int i = 0; i < count; i++) {
        printf("%s, %d, %s\n", pets[i].name, pets[i].age, pets[i].species);
    }

    // Free allocated memory
    free(pets);
    if (line) {
        free(line);
    }

    return 0;
}
