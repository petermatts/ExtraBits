#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// list as defined in lecture videos

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
    printf("EMPTY\n"); // addition I made for readablity
}

// sorts the list into ascending order
void *bubbleSort(list *h)
{
    list *head = h;
    list *next;
    int temp;

    while (!isEmpty(head))
    {
        next = head->next;
        while (!isEmpty(next))
        {
            // if head and next values are decending, swap them
            if (head->data > next->data)
            {
                temp = head->data;
                head->data = next->data;
                next->data = temp;
            }
            // continue bubbling next
            next = next->next;
        }
        head = head->next;
    }
}

// loops through the list and asserts that the list is sorted in ascending order
void proveSorted(list *h)
{
    list *head = h;
    list *next;
    while (!isEmpty(head))
    {
        next = head->next;
        if (!isEmpty(next) && next->data < head->data)
            assert(0);
        head = head->next;
    }
}

int main(void)
{
    // create an array of random numbers
    int arr[100];
    for (int i = 0; i < 100; i++)
        arr[i] = rand() % 100;

    // make list from array of random numbers
    list *nums = arrToList(arr, 100);
    printList(nums, "List");
    bubbleSort(nums);
    proveSorted(nums);
    printList(nums, "Sorted List");
    return 0;
}