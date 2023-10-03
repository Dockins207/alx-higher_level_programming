#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @f: integer
 * @next: points leadint to the next node
 * Description: singly linked list node
 */
typedef struct listint_s
{
    int f;
    struct listint_s *next;
} listint_t;
#endif
