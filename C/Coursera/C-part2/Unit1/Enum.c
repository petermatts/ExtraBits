#include <stdio.h>

enum day
{
    sun,
    mon,
    tue,
    wed,
    thu,
    fri,
    sat
}; // declare type

typedef enum day day;

void printDay(day d)
{
    switch (d)
    {
    case sun:
        printf(" Sunday ");
        break;
    case mon:
        printf(" Monday ");
        break;
    case tue:
        printf(" Tuesday ");
        break;
    case wed:
        printf(" Wednesday ");
        break;
    case thu:
        printf(" Thursday ");
        break;
    case fri:
        printf(" Friday ");
        break;
    case sat:
        printf(" Saturday ");
        break;
    default:
        printf("%d is an error", d);
    }
}

enum day nextDay(day d)
{
    return (d + 1) % 7;
}

int main(void)
{
    day today = fri;
    printDay(today);
    printf("\n\n");
    printDay(7);
    printf("\n\n");
    printDay(nextDay(today));
    printf("\n\n");
    return 0;
}
