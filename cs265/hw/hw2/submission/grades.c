// Author: Tony K. Okeke
// Date:   03.13.2024

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include "ll.h"
#include "utils.h"
#include "mystring.h"

int main(int argc, char* argv[]) {
    // check for correct number of arguments
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <database_file>\n", argv[0]);
        return 1;
    }

    // open the database file
    char* databaseFile = argv[1];
    FILE* fp = fopen(databaseFile, "r");
    if (fp == NULL) {
        fprintf(stderr, "Error: Unable to open database file '%s'\n", databaseFile);
        return 1;
    }

    // initialize the linked list
    LinkedList gradeList;
    initLL(&gradeList);

    // read existing grades from the database file
    char line[256];
    while (fgets(line, sizeof(line), fp) != NULL) {
        GradeEntry grade;
        if (parseLine(line, grade.studentId, grade.assignmentName, &grade.grade)) {
            appendNode(&gradeList, &grade);
        }
    }
    fclose(fp);

    // read commands from stdin
    char command[256];
    while (fgets(command, sizeof(command), stdin) != NULL) {
        command[mystrlen(command) - 1] = '\0';  // Remove trailing newline

        if (mystrncmp(command, "print", 5) == 0) {
            printGrades(&gradeList);
        } else if (mystrncmp(command, "add", 3) == 0) {
            char* args = command + 4;
            GradeEntry grade;

            if (parseLine(args, grade.studentId, grade.assignmentName, &grade.grade)) {
                if (!isGradeExists(&gradeList, grade.studentId, grade.assignmentName)) {
                    appendNode(&gradeList, &grade);
                } else {
                    fprintf(stderr, "Error: Grade entry already exists for student ID '%s' and assignment '%s'\n",
                            grade.studentId, grade.assignmentName);
                }
            } else {
                fprintf(stderr, "Invalid argument\n");
            }
        } else if (mystrncmp(command, "remove", 6) == 0) {
            char* args = command + 7;
            char studentId[11];
            char assignmentName[21];
    
            if (parseRemoveArgs(args, studentId, assignmentName)) {
                removeNode(&gradeList, studentId, assignmentName);
            } else {
                fprintf(stderr, "Invalid argument\n");
            }
        } else if (mystrncmp(command, "stats", 5) == 0) {
            char* assignmentName = command + 6;
            printStats(&gradeList, assignmentName);
        } else {
            fprintf(stderr, "Error: Invalid command '%s'\n", command);
        }
    }

    if (!saveGrades(databaseFile, &gradeList)) {
        fprintf(stderr, "Error: Unable to save grades to database file '%s'\n", databaseFile);
        return 1;
    }

    freeLL(&gradeList);
    return 0;
}