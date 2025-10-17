/*
Sine and Cosine Table generator
29/12/2021
by Axel Fava
*/

// Including the necessary libraries
#include <stdio.h>
#include <math.h>

// Main Function
int main()
{

    // Variable declaration
    double value = 0.0;
    int i;

    //"For loop" of 101 iterations so Value goes from 0.00 to 1.00 in 0.01 steps
    for (i = 0; i <= 100; i++)
    {
        // The calculations are done inside the printf() function
        printf("Value = %lf \t Sine = %lf \t Cosine = %lf \n", value, sin(value), cos(value));
        // Value is incremented at the end of the loop
        value += 0.01;
    }

    // End of main
    return 0;
}