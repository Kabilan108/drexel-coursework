// Author: Tony K. Okeke
// Date:   03.08.2024

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

typedef struct Pet Pet;
struct Pet {
    char name[16];
    int age;
    char species[16];
};

typedef struct Node Node;
struct Node {
    Pet pet;
    Node *next;
};


// initialize a new linked list with a single node
Node* llCreate(Pet* pet) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    if (newNode  == NULL) {
        printf("Error allocating memory\n");
        return NULL;
    }
    newNode->pet = *pet;
    newNode->next = NULL;
    return newNode;
}


// append a value to the linked list
Node* llAppend(Node* head, Pet* pet) {
    Node* newNode = llCreate(pet);
    if (newNode == NULL) {
        return NULL;
    }
    if (head == NULL) {
        return newNode;
    }

    Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    newNode->next = NULL;
    return head;
}


// delete list and free memory
void llFree(Node* head) {
    while (head != NULL) {
        Node* next = head->next;
        free(head);
        head = next;
    }
}


int main(int argc, char* argv[]) {
    ssize_t read;
    size_t len = 0;
    char* line = NULL;
    Node* head = NULL;

    while ((read = getline(&line, &len, stdin)) != -1) {
        // initialize new pet
        Pet* pet = malloc(sizeof(Pet));
        if (pet == NULL) {
            fprintf(stderr, "Error allocating memory\n");
            free(line);
            llFree(head);
            return 1;
        }

        // read pet name
        if (read > 0 && read < 16) {
            strcpy(pet->name, line);
            pet->name[strcspn(pet->name, "\n")] = '\0';
        }
        
        // read pet age
        if (getline(&line, &len, stdin) != -1) {
            pet->age = atoi(line);
        } else {
            fprintf(stderr, "Invalid input format\n");
            free(pet);
            free(line);
            llFree(head);
            return 1;
        }

        // read pet species
        if (getline(&line, &len, stdin) != -1 && read < 16) {
            strcpy(pet->species, line);
            pet->species[strcspn(pet->species, "\n")] = '\0';
        } else {
            fprintf(stderr, "Invalid input format\n");
            free(pet);
            free(line);
            llFree(head);
            return 1;
        }

        // append new pet to linked list
        head = llAppend(head, pet);
        free(pet);
    }

    // print pets, free memory
    while (head != NULL) {
        printf("%s, %d, %s\n", head->pet.name, head->pet.age, head->pet.species);
        Node* next = head;
        head = head->next;
        free(next);
    }

    free(line);
    return 0;
}
