#include <stdio.h>
#include <ctype.h>

#define MAX_LEN 1000
#define EMPTY -1
#define FULL (MAX_LEN - 1)

typedef struct stack
{
    char s[MAX_LEN];
    int top;
} stack;

void reset(stack *stk) { stk->top = EMPTY; }
void push(char c, stack *stk)
{
    stk->top++;
    stk->s[stk->top] = c;
}

char pop(stack *stk) { return (stk->s[stk->top--]); }
char top(stack *stk) { return (stk->s[stk->top]); }

int isEmpty(const stack *stk) { return (stk->top == EMPTY); }
int isFull(const stack *stk) { return (stk->top == FULL); }

int main(void)
{
    stack s;
    char *str = "!!dlroW olleH";
    char revStr[20];
    int i = 0;
    reset(&s);
    printf("Original is: %s\n", str);
    while (str[i] != '\0')
    {
        // printf("%c\n", str[i]);
        push(str[i++], &s);
    }
    i = 0;
    while (!isEmpty(&s) && i < 13)
        revStr[i++] = pop(&s);

    // printf("%d\n", i);
    printf("Reverse is: %s\n", revStr);
    return 0;
}