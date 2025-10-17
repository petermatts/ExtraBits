#include <stdio.h>

int main()
{
    int i = 1, j = 2;
    int n;
    n = (i < j);
    printf("%d\n", n);
    n = (i == j) ? 4 : (i < j) ? 3
                               : 5;
    printf("%d\n", n);
    n = (i, j);
    printf("%d\n", n);
    n = i, j + 1;
    printf("%d\n", n);
    n = (i < j) ? 4 : 6;
    printf("%d\n", n);
}