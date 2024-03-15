// Author: Tony K. Okeke
// Date:   03.14.2024

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include "ll.h"
#include "mystring.h"

int main(int argc, char* argv[]) {
    LinkedList* list = malloc(sizeof(LinkedList));
    initLL(list);

    ssize_t read;
    size_t len = 0;
    char* line = NULL;

    while ((read = getline(&line, &len, stdin)) != -1) {
        GradeEntry* grade = malloc(sizeof(GradeEntry));
        sscanf(line, "%s %s %hu", grade->studentId, grade->assignmentName, &grade->grade);
        appendNode(list, grade);
        free(grade);
    }

    Node* current = list->head;
    while (current != NULL) {
        printf("%s %s %d\n", current->grade.studentId, current->grade.assignmentName, current->grade.grade);
        current = current->next;
    }

    freeLL(list);
    free(line);
    free(list);

    return 0;
}

