#ifndef H_LISTS_H
#define H_LISTS_H

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * struct listint_s - singly link list.
 * @n: int.
 * @next: point to the next node.
 *
 * Description: singly linked list node structure.
 * for Python - Data Structures: Lists, Tuples project Tasks.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void reverse_listint(listint_t **head);
size_t print_listint(const listint_t *h);

void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif /* H_LISTS_H */
