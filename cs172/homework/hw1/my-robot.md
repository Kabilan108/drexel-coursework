# My Robot

In this part of the assignment we will practice using a class that has been given to us.

You are provided with a file robot.py (see attached file later). This file contains code that implements a very basic Robot object. It has a constructor, getter and setter methods. Take a look at the Robot class and familiarize yourself with those methods.

Your task is to write the main routine that creates a Robot object, prints the initial state of the object, moves the Robot forward some distance, displays the current state of the Robot after moving forward, charges the Robot's battery and then displays the state of the Robot after charging its battery.

Here are some additional specifications:

- The user of the program must provide the robot's initial battery level.
  - The battery level is a float value between 0.00 and 10.00.
  - You must use loops and try/except for the battery level validation.
- Instantiate a Robot object and use the initial battery level provided by the user.
- Display the Robot's current battery level and speed.
  - Values must be displayed with 2 decimal places after the decimal point.
- The user should now provide a distance for the Robot to move forward.
  - The distance is an integer value between 0 and 20.
  - You must use loops and try/except for the distance validation.
- Make the Robot move forward.
- Display the Robot's current battery level, distance traveled, current speed, and how much time would be needed to return to home base.
  - Battery level, speed, and time values must be displayed with 2 decimal places after the decimal point.
- Now the Robot's battery needs to be re-charged. Ask the user to enter a amount of charge
  - The amount entered should float value between 0.00 and 10.00. This value must be validated.
- Charge the Robot.
- Display the Robot's current battery level, current speed, and how much time would be needed to return to home base.
  - Battery level, speed, and time values must be displayed with 2 decimal places after the decimal point.

**Notes:**

- You are not allowed to modify the robot.py file or the Robot class.
- Make sure you include a header comment at the top of your file.
- *OPTIONAL:* you may write functions as you see fit to help with tasks such as input validation.

Below there’s a sample run:

```
Enter the robot's current battery's level (a value between 0 and 10.00): 3.00

Robot's current battery level: 3.00
Robot's current speed: 18.00

Enter the distance to move forward (a value between 0 and 20): 9

Robot's current battery level: 0.30
Robot's distance traveled: 9
Robot's current speed: 0.18
Time needed to go back to base: 50.00

Enter the amount to charge Robot's battery (a value between 0 and 10.00): 5

After recharging the battery:
Robot's current battery level: 5.30
Robot's current speed: 56.18
Time needed to go back to base: 0.16
```

**Notes:**

- You may find the following site useful to compare your output against the expected program output: [Diffchecker](https://www.diffchecker.com/)
- The purpose of this problem is to practice using classes and modules.
- Please make sure to submit a well-written program. Good identifier names, useful comments, and spacing will be some of the criteria that will be used when grading this assignment.
- This assignment can be and must be solved using only the materials that have been discussed in class. Do not look for alternative methods that have not been covered as part of this course.

How your program will be graded:

- correctness: the program works and performs all tasks correctly: 50% (autograded by Zybooks)
- complies with requirements (input validation using try/except and loops, correct use of loops, correct use of the Robot class methods ): 40% (TAs)
- code style: good variable names, header comment, other comments as needed, proper indentation and spacing: 10% (TAs)

