#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct list
{
    int data;
    struct list *next;
} list;

int isEmpty(const list *l) { return (l == NULL); }

list *createList(int d)
{
    list *head = malloc(sizeof(list));
    head->data = d;
    head->next = NULL;
    return head;
}

list *addToFront(int d, list *h)
{
    list *head = createList(d);
    head->next = h;
    return head;
}

list *arrToList(int d[], int size)
{
    list *head = createList(d[0]);
    int i;
    for (i = 1; i < size; i++)
        head = addToFront(d[i], head);
    return head;
}

void printList(list *h, char *title)
{
    printf("%s\n", title);
    while (h != NULL)
    {
        printf("%d : ", h->data);
        h = h->next;
    }
}

int main(void)
{
    list l;
    list *head = NULL;
    head = malloc(sizeof(list));
    printf("sizeof(list) = %lu\n", sizeof(list));
    head->data = 5;
    head->next = NULL;
    printList(head, "Single element list");
    printf("\n\n");
    return 0;
}