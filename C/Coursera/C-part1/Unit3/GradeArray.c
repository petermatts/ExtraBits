#include <stdio.h>

int main(void)
{
    const int SIZE = 5;
    int grades[5] = {78, 67, 92, 83, 88};
    // can declare an array of unspecified size like array[] = {...}
    // if declared like array[SIZE] = { 100 }, all elements will be initialized to 100

    double sum = 0.0;
    int i;

    printf("\nmy grades are:\n");
    for (i = 0; i < SIZE; i++)
        printf("%d\t", grades[i]);

    printf("\n\n");

    for (i = 0; i < SIZE; i++)
        sum += grades[i];

    printf("my average is %.2f\n\n", sum / SIZE);
}