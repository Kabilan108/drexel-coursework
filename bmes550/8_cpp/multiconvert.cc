/*
Write a function multiconvert.cc that takes from the command line a conversion
code and a number; and converts the given number according to the following
conversion rules:

code          conversion type            conversion rule
----    ----------------------------    ----------------
 f      Frenheit(F) to Celcius(C)         C = 5/9*(F-32)
 i      Inches(I) to centimeters(cm)     cm = 3/2*I
 m      miles(M) to kilometers(Km)       Km = 1.6*M
 p      pound(P) to kilograms(Kg)        Kg = 0.45*P

>> ./multiconvert f 20
20.00 farenheit to celsius: -6.67
*/

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <cstring>

int main(int argc, char **argv) {
    // Define code, a character pointer, pointing to an array of characters
    // and value
    char* code;
    float value;

    if (argc != 3) {
        printf("On the command line, you must provide a code and a number and");
        printf("nothing else.\n");
        return 1;
    }

    // argv[0] is the executable file name, argv[1] is the code, argv[2] is the
    // number
    code = argv[1];
    value = atof(argv[2]);

    if (strcmp(code, "f")==0) { //this is how you would ask if code is "f".
        printf("%.2f fahrenheit to celcius: %.2f\n", value, 5.0 / 9 * (value - 32));
    }
    else if(strcmp(code, "i")==0) {
        printf("%.2f inches to cm: %.2f\n", value, 3.0 / 2 * value);
    }
    else if (strcmp(code, "m") == 0) {
        printf("%.2f miles to km: %.2f\n", value, 1.6 * value);
    }
    else if (strcmp(code, "p") == 0) {
        printf("%.2f pounds to kg: %.2f\n", value, 0.45 * value);
    }
    else {
        printf("Error. Unknown code: %s\n", code);
        return 1;
    }

    return 0;
}