#include <stdio.h>

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
    sep,
    oct,
    nov,
    dec
} month;

typedef struct date
{
    month m;
    short date;
} date;

void printDate(date d)
{
    int i = d.date;

    // print dates in detail
    switch (d.m)
    {
    case jan:
        printf("January %d", i);
        break;
    case feb:
        printf("February %d", i);
        break;
    case mar:
        printf("March %d", i);
        break;
    case apr:
        printf("April %d", i);
        break;
    case may:
        printf("May %d", i);
        break;
    case jun:
        printf("June %d", i);
        break;
    case jul:
        printf("July %d", i);
        break;
    case aug:
        printf("August %d", i);
        break;
    case sep:
        printf("September %d", i);
        break;
    case oct:
        printf("October %d", i);
        break;
    case nov:
        printf("November %d", i);
        break;
    case dec:
        printf("December %d", i);
        break;
    default:
        printf("Error: invalid month occured");
    }
}

// function for alternate form of date printing
// numerically in the form mm/dd
void printDayNum(date d)
{
    printf("(%d/%d)", d.m + 1, d.date);
}

date nextDate(date d)
{
    date nextDay;
    // intialize nextDay to have same month and date+1
    nextDay.m = d.m;
    nextDay.date = d.date + 1;

    // assuming no leap year, next day will be march 1
    if (nextDay.date == 29 && d.m == feb)
    {
        nextDay.m = d.m + 1;
        nextDay.date = 1;
        return nextDay; // return and exit the function
    }

    // this switch is for reseting day to 1 and month to the
    // next month iff max days in a month are exceeded
    switch (d.m)
    {
    case jan:
    case mar:
    case may:
    case jul:
    case aug:
    case oct:
    case dec:
        if (nextDay.date == 32)
        {
            nextDay.date = 1;
            nextDay.m = (d.m + 1) % 12; // mod 12 to turn dec into jan
        }
        break;

    case apr:
    case jun:
    case sep:
    case nov:
        if (nextDay.date == 31)
        {
            nextDay.date = 1;
            nextDay.m = d.m + 1;
        }
        break;
    default:
        printf("This should not execute, because it is February");
    }

    // return and exit the function
    return nextDay;
}

void printTodayAndTomorrow(date d)
{
    printf("Today is: ");
    printDate(d);
    // printf("\t");
    // printDayNum(d);
    printf("\nTomorrow is: ");
    printDate(nextDate(d));
    // printf("\t");
    // printDayNum(nextDate(d));
    printf("\n\n");
}

int main(void)
{
    date day;

    // initialize day to 1/1
    day.m = jan;
    day.date = 1;
    printTodayAndTomorrow(day);

    // set day to 2/28
    day.m = feb;
    day.date = 28;
    printTodayAndTomorrow(day);

    // set day to 3/14
    day.m = mar;
    day.date = 14;
    printTodayAndTomorrow(day);

    // set day to 10/31
    day.m = oct;
    day.date = 31;
    printTodayAndTomorrow(day);

    // set day to 12/31
    day.m = dec;
    day.date = 31;
    printTodayAndTomorrow(day);

    return 0;
}
