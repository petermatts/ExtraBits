/* Conevert Fahrenheit to Celcius */
#include <stdio.h>

int main()
{
    int fahrenheit, celcius;
    printf("Enter fahrenheit integer value: ");
    scanf("%d", &fahrenheit);
    celcius = (fahrenheit - 32) / 1.8;
    printf("\n %d fahrenheit is %d celcius.\n", fahrenheit, celcius);
    return 0;
}