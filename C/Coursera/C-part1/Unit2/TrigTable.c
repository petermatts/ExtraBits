/*
 * TragTable.c
 * Prints a detailed table of values for sine and cosine values given input between 0 and 1;
 */

#include <stdio.h>
#include <math.h>

int main(void)
{
    // print table header
    printf("  x  |  sin(x)  |  cos(x)  \n");

    // for loop to print values of the table
    for (double i = 0; i < 1; i += 0.1)
    {
        // print grid line
        printf("-----+----------+----------\n");
        // print data row
        printf(" %.1lf | %lf | %lf \n", i, sin(i), cos(i));
    }

    // end
    return 0;
}