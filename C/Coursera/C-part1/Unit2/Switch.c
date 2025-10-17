#include <stdio.h>

int main(void)
{
    int i = 2;
    switch (i)
    {
    case 1:
        printf("case 1 \n");
        break;
    case 2:
        printf("case 2 \n");
    case 3:
        printf("case 3 \n");
        break;
    default:
        printf("default case \n");
    }
}