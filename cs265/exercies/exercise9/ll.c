// Author: Tony K. Okeke
// Date:   03-07-2024

#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
};


Node* prependLL(Node* head, int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Error allocating memory\n");
        return head;
    }
    newNode->data = data;
    newNode->next = head;
    return newNode;
}


Node* appendLL(Node* head, int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Error allocating memory\n");
        return head;
    }
    newNode->data = data;
    newNode->next = NULL;

    if (head == NULL) {
        return newNode;
    }

    Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = newNode;
    return head;
}


Node* deleteLL(Node* head, int index) {
    Node* current = head;
    int i = 0;

    // if index is 0, delete the head
    if (index == 0) {
        Node* temp = head;
        head = temp->next;
        free(temp);
        return head;
    }

    // walk to the node before the one to be deleted
    while (current->next != NULL && i < index - 1) {
        current = current->next;
        i++;
    }

    // if next is None, index DNE
    if (current->next == NULL) {
        return head;
    }

    Node* temp = current->next;
    current->next = temp->next;
    free(temp);
    return head;
}


Node* reverseLL(Node* head) {
    Node* current = head;
    Node* next = head->next;
    Node* prev = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}


int main(int argc, char* argv[]) {
    Node* head = NULL;

    // Test prependLL
    head = prependLL(head, 10);
    if (head != NULL && head->data == 10) {
        printf("prependLL Test 1 Passed\n");
    } else {
        printf("prependLL Test 1 Failed\n");
    }

    head = prependLL(head, 20);
    if (head != NULL && head->data == 20 && head->next->data == 10) {
        printf("prependLL Test 2 Passed\n");
    } else {
        printf("prependLL Test 2 Failed\n");
    }

    // Test appendLL
    head = appendLL(head, 30);
    Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    if (current->data == 30) {
        printf("appendLL Test 1 Passed\n");
    } else {
        printf("appendLL Test 1 Failed\n");
    }

    head = appendLL(head, 40);
    current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    if (current->data == 40) {
        printf("appendLL Test 2 Passed\n");
    } else {
        printf("appendLL Test 2 Failed\n");
    }

    // Test deleteLL
    head = deleteLL(head, 1); 
    if (head != NULL && head->data == 20 && head->next->data == 30) {
        printf("deleteLL Test 1 Passed\n");
    } else {
        printf("deleteLL Test 1 Failed\n");
    }

    head = deleteLL(head, 0);
    if (head != NULL && head->data == 30 && head->next->data == 40) {
        printf("deleteLL Test 2 Passed\n");
    } else {
        printf("deleteLL Test 2 Failed\n");
    }

    // Test reverseLL
    head = reverseLL(head);
    if (head != NULL && head->data == 40 && head->next->data == 30) {
        printf("reverseLL Test 1 Passed\n");
    } else {
        printf("reverseLL Test 1 Failed\n");
    }

    head = reverseLL(head);
    if (head != NULL && head->data == 30 && head->next->data == 40) {
        printf("reverseLL Test 2 Passed\n");
    } else {
        printf("reverseLL Test 2 Failed\n");
    }

    // Clean up
    while (head != NULL) {
        Node* temp = head;
        head = head->next;
        free(temp);
    }

}