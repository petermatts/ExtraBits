#include <stdio.h>
#include <limits.h>

// function for computing the sum of the array
double sum(int data[], int size)
{
    double sum = 0;
    for (int i = 0; i < size; i++)
        sum += data[i];
    return sum;
}

// function for computing the max value in the array
int max(int data[], int size)
{
    int max = INT_MIN;
    for (int i = 0; i < size; i++)
        if (data[i] > max)
            max = data[i];
    return max;
}

// function for computing the average (in a double) of the array values
double average(int data[], int size) { return sum(data, size) / size; }

// function to print array
void printArray(int data[], int size)
{
    printf("[");
    for (int i = 0; i < size - 1; i++)
        printf("%d, ", data[i]);
    printf("%d]\n", data[size - 1]);
}

int main(void)
{
    // declare and initialize variables/pointers
    FILE *ifp = fopen("HW3_INPUT.txt", "r");
    FILE *ofp = fopen("answer-hw3.txt", "w");
    const int SIZE;
    int i = 0;
    int data[100] = {};

    fscanf(ifp, "%d", &SIZE); // get the size of the array

    // fill array with data
    while (!feof(ifp))
    {
        fscanf(ifp, "%d", &data[i]);
        i++;
    }

    // print output to terminal
    printf("Below is the array of %d numbers\n", SIZE);
    printArray(data, SIZE);
    printf("The max value in the array is: %d\n", max(data, SIZE));
    printf("The average value in the array is: %.4lf\n", average(data, SIZE));

    // write to output file
    fputs("Below is the array of ", ofp);
    fprintf(ofp, "%d numbers:\n[", SIZE);
    for (int i = 0; i < SIZE - 1; i++)
        fprintf(ofp, "%d, ", data[i]);
    fprintf(ofp, "%d]\nThe max value in the array is: ", data[SIZE - 1]);
    fprintf(ofp, "%d\nThe average value in the array is: ", max(data, SIZE));
    fprintf(ofp, "%.4lf\n", average(data, SIZE));

    // close file streams and terminate program
    fclose(ifp);
    fclose(ofp);
    return 0;
}