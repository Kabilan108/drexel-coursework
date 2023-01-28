#File Name:   student.py
#Purpose:     Class to represent a student
#             A student has a name (non mutable)
#                           a number of total credits earned
#                           a number of quality points
#             At any given time we may need to:
#                           obtain the student's name
#                           find out how many credits the student has earned
#                           the student's current GPA
#             A student earns credits and quality points depending on the course final grade
#Author:      Adelaida Medlock
#Date:        January 19, 2021

class Student :
    # constructor
    def __init__(self, name) :
        self.__name = name
        self.__totalCredits = 0.0
        self.__qualityPoints = 0.0
    
    # getters / accessors / inspectors
    def getName(self) :
        return self.__name
    
    def getTotalCredits(self) :
        return self.__totalCredits
    
    def getGPA(self) :
        if self.__totalCredits == 0.0 :
            return 0.0
        else:
            return self.__qualityPoints / self.__totalCredits
    
    # mutators / setters
    def earnCredits(self, credits, grade) :
        grade = grade.upper()
        if grade == 'A' :
            qPoints = 4.0
        elif grade == 'B' :
            qPoints = 3.0
        elif grade == 'C' :
            qPoints = 2.0
        elif grade == 'D' :
            qPoints = 1.0
        else : #grade == 'F':
            qPoints = 0.0
        
        self.__totalCredits = self.__totalCredits + credits
        self.__qualityPoints = self.__qualityPoints + qPoints * credits
        
    # overloaded __str__ method
    def __str__(self):
        myStr = "Student's name: " + self.__name + '\n'
        myStr = myStr + 'Credits Earned: ' + str(self.__totalCredits) + '\n'
        myStr = myStr + "Student's GPA:  " + str(self.getGPA()) + '\n'
        return (myStr)
    
    # overloaded __eq__ method to be able to use ==
    def __eq__(self, other):
        name = self.__name == other.getName()
        credits = self.__totalCredits == other.getTotalCredits()
        gpa = self.getGPA() == other.getGPA()
        return (name and credits and gpa)
    
    # overloaded __ne__ method to be able to use !=
    def __ne__ (self, other):
        name = self.__name != other.getName()
        credits = self.__totalCredits != other.getTotalCredits()
        gpa = self.getGPA() != other.getGPA()
        return name or credits or gpa


if __name__== "__main__":
    
    from random import randint
    
    # create two students
    joe = Student('Joe')
    jane = Student('Jane')
    
    # each student takes 5 courses
    for i in range(0, 5):
        gradeCode = ord('A') + randint(0, 3)
        grade = chr(gradeCode)
        joe.earnCredits(3.0, grade)
        gradeCode = ord('A') + randint(0, 3)
        grade = chr(gradeCode)
        jane.earnCredits(3.0, grade)
    
    
    #print the students' gpa - using getters
    print("Joe's gpa:", joe.getGPA())
    print("Jane's gpa:", jane.getGPA())
    print()
    
    # print the objects: using overloaded operator
    print(joe)
    print(jane)
    
    # comparing objects
    if joe == jane :
        print ('Both objects have the same values for their attributes')
    elif joe!= jane :
        print ('These objects have the different values for their attributes')
        
    
                   
        