// Author: Tony K. Okeke
// Date:   03.13.2024

#ifndef UTILS_H
#define UTILS_H
    #include "ll.h"

    bool parseLine(const char* line, char* studentId, char* assignmentName, unsigned short* grade);
    bool parseRemoveArgs(const char* args, char* studentId, char* assignmentName);
    bool isGradeExists(LinkedList* list, const char* studentId, const char* assignmentName);
    bool saveGrades(const char* databaseFile, LinkedList* list);
    
    void printGrades(LinkedList* list);
    void printStats(LinkedList* list, const char* assignmentName);
#endif
