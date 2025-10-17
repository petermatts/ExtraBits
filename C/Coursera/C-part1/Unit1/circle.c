/* Input radius, output area */

#include <stdio.h>
#define PI 3.14159

int main()
{
    double area = 0.0, radius = 0.0;
    printf("Enter a radius: ");
    scanf("%lf", &radius);
    area = PI * radius * radius;
    printf("radius of %lf units: area is %lf sq units\n", radius, area);
    return 0;
}