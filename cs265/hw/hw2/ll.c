// Author: Tony K. Okeke
// Date:   03.13.2024

#include <stddef.h>
#include <stdlib.h>
#include <string.h>

#include "ll.h"

// create new LL node
Node* createNode(GradeEntry* grade) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Error allocating memory\n");
        return NULL;
    }
    newNode->grade = *grade;
    newNode->next = NULL;
    return newNode;
}

// initialize LL
void initLL(LinkedList* list) {
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}

// append node to LL
void appendNode(LinkedList* list, GradeEntry* grade) {
    Node* newNode = createNode(grade);
    if (newNode == NULL) {
        return;
    }
    if (list->head == NULL) {
        list->head = newNode;
        list->tail = newNode;
    } else {
        list->tail->next = newNode;
        list->tail = newNode;
    }
    list->size++;
}

// remove node from LL
void removeNode(LinkedList* list, char* studentId, char* assignmentName) {
    Node* temp = list->head;
    Node* prev = NULL;
    while (temp != NULL) {
        // TODO: replace strcmp with mystrcmp
        if (
            strcmp(temp->grade.studentId, studentId) == 0 && 
            strcmp(temp->grade.assignmentName, assignmentName) == 0
        ) {
            if (prev == NULL) {
                // removing head
                list->head = temp->next;
            } else {
                prev->next = temp->next;
            }
            if (temp == list->tail) {
                // removing tail
                list->tail = prev;
            }
            free(temp);
            list->size--;
            return;
        }
        prev = temp;
        temp = temp->next;
    }    
}

