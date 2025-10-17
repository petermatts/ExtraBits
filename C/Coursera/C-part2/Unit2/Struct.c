#include <stdio.h>

struct card
{
    int pips;
    char suit;
};

typedef struct card card;

int main()
{
    card c1; // 3 of hearts
    c1.pips = 3;
    c1.suit = 'H';

    card *c1ptr = &c1;
    c1ptr->pips = 5;
    c1ptr->suit = 'S'; // now it is the 5 of spades

    // . operator gets element
    // -> operator sets element

    return 0;
}