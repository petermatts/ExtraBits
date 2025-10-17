#include <stdio.h>

double average_grades(int how_many, int grades[])
{
    int i;
    double sum = 0.0;
    for (i = 0; i < how_many; i++)
        sum += grades[i];
    return (sum / how_many);
}

void print_grades(int how_many, int grades[])
{
    int i;
    printf("I have %d grades\n", how_many);
    for (i = 0; i < how_many; i++)
        printf("%d\t", grades[i]);

    printf("\n");
}

#define SIZE 5
int main(void)
{
    // const int SIZE = 5;
    int grades[SIZE] = {78, 67, 92, 83, 88};

    print_grades(SIZE, grades);
    printf("my average is %.2f\n\n", average_grades(SIZE, grades));
}