/*
   this program prints the date
   Jan. 6, 2022
*/

#include <stdio.h>
#include <math.h>
#define SMONTH 30
#define LMONTH 31
#define FEB 28

typedef enum month
{
    jan,
    feb,
    mar,
    apr,
    may,
    jun,
    jul,
    aug,
    sept,
    oct,
    nov,
    dec
} month;
typedef struct date
{
    month m;
    int d;
} date;

date next_day(date dt)
{
    date next_date;
    next_date.m = dt.m;
    next_date.d = dt.d;
    switch (dt.m)
    {
    case jan:
        if (dt.d == LMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % LMONTH;
        break;
    case feb:
        if (dt.d == FEB)
            next_date.m++;
        next_date.d = (next_date.d + 1) % FEB;
        break;
    case mar:
        if (dt.d == LMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % LMONTH;
        break;
    case apr:
        if (dt.d == SMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % SMONTH;
        break;
    case may:
        if (dt.d == LMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % LMONTH;
        break;
    case jun:
        if (dt.d == SMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % SMONTH;
        break;
    case jul:
        if (dt.d == LMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % LMONTH;
        break;
    case aug:
        if (dt.d == LMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % LMONTH;
        break;
    case sept:
        if (dt.d == SMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % SMONTH;
        break;
    case oct:
        if (dt.d == LMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % LMONTH;
        break;
    case nov:
        if (dt.d == SMONTH)
            next_date.m++;
        next_date.d = (next_date.d + 1) % SMONTH;
        break;
    case dec:
        if (dt.d == LMONTH)
            next_date.m = jan;
        next_date.d = (next_date.d + 1) % LMONTH;
        break;
    default:
        printf("not a valid month");
    }
    return next_date;
}

void printdate(date date)
{
    switch (date.m)
    {
    case jan:
        printf("January");
        break;
    case feb:
        printf("February");
        break;
    case mar:
        printf("March");
        break;
    case apr:
        printf("April");
        break;
    case may:
        printf("May");
        break;
    case jun:
        printf("June");
        break;
    case jul:
        printf("July");
        break;
    case aug:
        printf("August");
        break;
    case sept:
        printf("september");
        break;
    case oct:
        printf("October");
        break;
    case nov:
        printf("November");
        break;
    case dec:
        printf("December");
        break;
    default:
        printf("invalid month");
    }
    printf(" %d\n", date.d);
}

void output(date dt)

{
    printf("Date is : ");
    printdate(dt);
    printf("Next day is : ");
    printdate(next_day(dt));
    printf("\n");
}

int main()

{
    date first_date, second_date, third_date, fourth_date, fifth_date, sixth_date;

    first_date.m = jan;
    first_date.d = 1;
    second_date.m = jan;
    second_date.d = 2;
    third_date.m = feb;
    third_date.d = 28;
    fourth_date.m = mar;
    fourth_date.d = 14;
    fifth_date.m = oct;
    fifth_date.d = 31;
    sixth_date.m = dec;
    sixth_date.d = 31;
    output(first_date);
    output(second_date);
    output(third_date);
    output(fourth_date);
    output(fifth_date);
    output(sixth_date);
    return 0;
}
