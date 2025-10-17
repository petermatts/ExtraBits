#include <stdio.h>

// define constants
#define SIZE 52
// #define HEART 'h'
// #define DIAMOND 'd'
// #define CLUB 'c'
// #define SPADE 's'
#define ACE 1
#define JACK 11
#define QUEEN 12
#define KING 13

typedef enum Suit
{
    heart,
    diamond,
    club,
    spade
} Suit;

// define a card struct
typedef struct card
{
    Suit suit;
    int rank;
} card;

// define a deck struct
typedef struct deck
{
    card c[SIZE];
} deck;

deck makeDeck()
{
    deck d;
    int r = 1;
    int s;
    for (int i = 0; i < SIZE; i++)
    {
        if (i <= 12)
            s = heart;
        else if (i > 12 && i <= 25)
            s = diamond;
        else if (i > 25 && i <= 38)
            s = club;
        else
            s = spade;
        card c;
        c.rank = r;
        c.suit = s;
        d.c[i] = c;

        r = (r + 1) % 14;
        if (r == 0)
            r++;
    }

    return d;
}

void shuffle(deck d)
{
}

void printCard(card c)
{
    // printf("%c\t%d\n", c.suit, c.rank);
    switch (c.rank)
    {
    case ACE:
        printf("ace ");
        break;
    case JACK:
        printf("jack ");
        break;
    case QUEEN:
        printf("queen ");
        break;
    case KING:
        printf("king ");
        break;
    default:
        printf("%d ", c.rank);
    }
    switch (c.suit)
    {
    case heart:
        printf("of hearts\n");
        break;
    case diamond:
        printf("of diamonds\n");
        break;
    case club:
        printf("of clubs\n");
        break;
    case spade:
        printf("of spades\n");
        break;
    default:
        printf("Error: invalid card\n");
    }
}
void printDeck(deck d)
{
    for (int i = 0; i < SIZE; i++)
        printCard(d.c[i]);
}

int main()
{
    deck d = makeDeck();
    printDeck(d);
    return 0;
}