#include <stdio.h>
#define PI 3.14159
int main(void)
{
    double radius;
    printf("Enter radius: ");
    scanf("%lf", &radius);
    printf("volume is : %g \n\n", (4.0 / 3.0) * (PI) * (radius * radius * radius));
    return 0;
}