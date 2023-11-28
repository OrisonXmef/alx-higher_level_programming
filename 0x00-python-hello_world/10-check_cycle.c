#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
struct listint_s {
    int n;
    struct listint_s *next;
};

typedef struct listint_s listint_t;

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list) {
    listint_t *tortoise = list;
    listint_t *hare = list;

    while (tortoise != NULL && hare != NULL && hare->next != NULL) {
        tortoise = tortoise->next;
        hare = hare->next->next;

        /* If the pointers meet, there is a cycle. */
        if (tortoise == hare)
            return 1;
    }

    /* If the loop exits, there is no cycle. */
    return 0;
}
