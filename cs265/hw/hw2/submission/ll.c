// Author: Tony K. Okeke
// Date:   03.13.2024

#include <stddef.h>
#include <stdlib.h>

#include "ll.h"
#include "mystring.h"

// initialize LL
void initLL(LinkedList* list) {
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}

// create new LL node
Node* createNode(GradeEntry* grade) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    if (newNode == NULL) {
        return NULL;
    }
    newNode->grade = *grade;
    newNode->next = NULL;
    return newNode;
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
    Node* current = list->head;
    Node* prev = NULL;
    while (current != NULL) {
        if (
            mystrcmp(current->grade.studentId, studentId) == 0 && 
            mystrcmp(current->grade.assignmentName, assignmentName) == 0
        ) {
            if (prev == NULL) {
                // removing head
                list->head = current->next;
            } else {
                // update node references
                prev->next = current->next;
            }
            if (current == list->tail) {
                // removing tail
                list->tail = prev;
            }
            free(current);
            list->size--;
            return;
        }
        prev = current;
        current = current->next;
    }    
}

// free LL
void freeLL(LinkedList* list) {
    Node* head = list->head;
    Node* next;
    while (head != NULL) {
        next = head->next;
        free(head);
        head = next;
    }
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}
