#include <stdio.h>

// function to print int arrays
void printArr(int size, int arr[])
{
    printf("[");
    for (int i = 0; i < size - 1; i++)
        printf("%d, ", arr[i]);
    printf("%d]\n", arr[size - 1]);
}

// Function for computing the average of an int array
double avg(int size, int arr[])
{
    double sum = 0.0;
    for (int i = 0; i < size; i++)
        sum += arr[i];
    return sum / size;
}

int main(void)
{
    // file name arguement must match name of file data is stored in
    FILE *weights = fopen("elephant_seal_data.txt", "r"); // open file stream to read only
    // Print message if error occurs opening file
    if (weights == NULL)
    {
        printf("Error: could not open file");
        return 0;
    }

    int data[1000] = {}; // array to store weight data in
    int i = 0;
    while (!feof(weights))
    {
        fscanf(weights, "%d", &data[i]);
        i++; // increment to track number of elements in array
    }
    fclose(weights); // close the file stream

    const int SIZE = i - 1; // decrement to account for additional eof element

    // printArr(SIZE, data);
    const double average = avg(SIZE, data);
    printf("\nThe average weight is: %.3lf\n", average);

    // end of program
    return 0;
}