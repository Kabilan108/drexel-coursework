// Author: Tony K. Okeke
// Date:   03.13.2024

#ifndef LL_H
#define LL_H
    typedef struct GradeEntry GradeEntry;
    struct GradeEntry {
        char studentId[11];
        char assignmentName[21];
        unsigned short grade;
    };

    typedef struct Node Node;
    struct Node {
        GradeEntry grade;
        Node* next;
    };

    typedef struct LinkedList LinkedList;
    struct LinkedList {
        Node* head;
        Node* tail;
        int size;
    };

    void initLL(LinkedList* list);

    Node* createNode(GradeEntry* grade);

    void appendNode(LinkedList* list, GradeEntry* grade);

    void removeNode(LinkedList* list, char* studentId, char* assignmentName);

    void freeLL(LinkedList* list);
#endif
