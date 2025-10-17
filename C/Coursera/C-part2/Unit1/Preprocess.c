#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_WEIGHT 8800
#define MIN_WEIGHT 4400

#define RANGE 4400
#define POPULATION 1000
#define WEIGHT_OVER rand() % RANGE;
#define WEIGHT WEIGHT_OVER + MIN_WEIGHT;
#define FILL                         \
    for (i = 0; i < POPULATION; i++) \
        data[i] = WEIGHT;

void printData(int d[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        printf("%.4d\t", d[i]);
        if ((i + 1) % 10 == 0)
            printf("\n");
    }
}

int main()
{
    int i;
    int data[POPULATION];
    srand(time(0));
    FILL;
    printData(data, POPULATION);
    printf("\n\n");
    return 0;
}