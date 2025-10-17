#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void printArray(int size, int data[], char *str)
{
    int i;
    printf("%s", str);

    for (i = 0; i < size; i++)
        printf("%d\t", data[i]);
}

void bubble(int data[], int size)
{
    int i, j;
    // int go_on;

    for (i = 0; i < size; i++)
    {
        // print_array(size, data, "\ninside bubble\n");
        printArray(size, data, "\n");
        // printf("i = %d, input any int to continue", i);
        // scanf("%d", go_on);
        for (j = size - 1; j > i; j--)
            if (data[j - 1] > data[j])
                swap(&data[j - 1], &data[j]);
    }
}

int main(void)
{
    const int SIZE = 5;
    int grades[5] = {78, 67, 92, 83, 88};
    bubble(grades, SIZE);

    // calculate the size of the array
    // const int size = sizeof(grades) / sizeof(int);

    return 0;
}
