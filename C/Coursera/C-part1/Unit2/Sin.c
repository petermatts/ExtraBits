#include <stdio.h>
#include <math.h>

int main(void)
{
    // variable for comuting sine value
    double x;

    // prompt for input
    printf("Enter an x in range (0,1) to compute sin(x): ");

    // scan variable
    scanf("%lf", &x);

    // check for x out the range (0,1)
    if (x >= 1 || x <= 0)
    {
        // display error message
        printf("Sorry, your value is out of the specified range.\n");
        return 0;
    }

    // x is in range, display calculated sine value output
    printf("sin(%g) = %g\n", x, sin(x));
    return 0;
}