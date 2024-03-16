// Author: Tony K. Okeke
// Date:   03.13.2024

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h> // Include for mkstemp

#include "utils.h"
#include "mystring.h"

// Parse a line from the database file
bool parseLine(
    const char* line, 
    char* studentId, 
    char* assignmentName, 
    unsigned short* grade
) {
    int idLen = 0;
    int nameLen = 0;
    int gradeVal = 0;

    // read the student ID, up to the ':' character
    const char* p = line;
    while (*p != ':' && *p != '\0' && idLen < 10) {
        studentId[idLen++] = *p++;
    }
    if (*p != ':' || idLen != 10) {
        return false;
    }
    studentId[idLen] = '\0';

    // read the assignment name, up to the ':' character
    p++;
    while (*p != ':' && *p != '\0' && nameLen < 20) {
        assignmentName[nameLen++] = *p++;
    }
    if (*p != ':' || nameLen == 0) {
        return false;
    }
    assignmentName[nameLen] = '\0';

    // read the grade, up to the newline character
    p++;
    while (*p >= '0' && *p <= '9') {
        gradeVal = gradeVal * 10 + (*p - '0');  
        p++;
    }
    if (*p == '\n') p++; // ignore the newline character if present
    if (*p != '\0' || gradeVal < 0 || gradeVal > 100) {
        return false;
    }
    *grade = (unsigned short) gradeVal;

    return true;
}

// Parse the arguments for the remove command
bool parseRemoveArgs(const char* args, char* studentId, char* assignmentName) {
    int idLen = 0;
    int nameLen = 0;

    // read the student ID, up to the ':' character
    const char* p = args;
    while (*p != ':' && *p != '\0' && idLen < 10) {
        studentId[idLen++] = *p++;
    }
    if (*p != ':' || idLen != 10) {
        return false;
    }
    studentId[idLen] = '\0';

    // read the assignment name, up to the ':' character
    p++;
    while (*p != '\0' && nameLen < 20) {
        assignmentName[nameLen++] = *p++;
    }
    if (nameLen == 0) {
        return false;
    }
    assignmentName[nameLen] = '\0';

    return true;
}

// traverse the list, print the grades
void printGrades(LinkedList* list) {
    printf("Student ID | Assignment Name      | Grade\n");
    printf("-----------------------------------------\n");

    Node* current = list->head;
    while (current != NULL) {
        printf("%-10s | %-20s | %hu\n",
               current->grade.studentId,
               current->grade.assignmentName,
               current->grade.grade);
        current = current->next;
    }
}

// compute & report statistics for a specified assignment
void printStats(LinkedList* list, const char* assignmentName) {
    unsigned short minGrade = 100;
    unsigned short maxGrade = 0;
    int totalGrade = 0;
    int count = 0;

    Node* current = list->head;
    while (current != NULL) {
        if (mystrcmp(current->grade.assignmentName, assignmentName) == 0) {
            unsigned short grade = current->grade.grade;
            if (grade < minGrade) {
                minGrade = grade;
            }
            if (grade > maxGrade) {
                maxGrade = grade;
            }
            totalGrade += grade;
            count++;
        }
        current = current->next;
    }

    if (count == 0) {
        fprintf(stderr, "Error: No grades found for assignment '%s'\n", assignmentName);
        return;
    }

    double meanGrade = (double) totalGrade / count;

    printf("Grade statistics for %s\n", assignmentName);
    printf("Min:  %hu\n", minGrade);
    printf("Max:  %hu\n", maxGrade);
    printf("Mean: %.2f\n", meanGrade);
}

// check if a grade exists in the list
bool isGradeExists(LinkedList* list, const char* studentId, const char* assignmentName) {
    Node* current = list->head;
    while (current != NULL) {
        if (mystrcmp(current->grade.studentId, studentId) == 0 &&
            mystrcmp(current->grade.assignmentName, assignmentName) == 0) {
            return true;
        }
        current = current->next;
    }
    return false;
}

// save the grades to the database file
bool saveGrades(const char* databaseFile, LinkedList* list) {
    // create temporary file with a unique name
    char tempFileTemplate[] = "gradesXXXXXX"; 
    int tempFd = mkstemp(tempFileTemplate); 
    if (tempFd == -1) {
        fprintf(stderr, "Error: Unable to create unique temporary file\n");
        return false;
    }

    FILE* fp = fdopen(tempFd, "w"); 
    if (fp == NULL) {
        fprintf(stderr, "Error: Unable to open temporary file '%s'\n", tempFileTemplate);
        close(tempFd); 
        return false;
    }

    // write the grades to the temporary file
    Node* current = list->head;
    while (current != NULL) {
        fprintf(fp, "%s:%s:%hu\n",
                current->grade.studentId,
                current->grade.assignmentName,
                current->grade.grade);
        current = current->next;
    }
    fclose(fp); 

    // remove the original file and rename the temporary file
    if (remove(databaseFile) != 0 || rename(tempFileTemplate, databaseFile) != 0) {
        fprintf(stderr, "Error: Unable to update database file '%s'\n", databaseFile);
        remove(tempFileTemplate); 
        return false;
    }

    return true;
}
