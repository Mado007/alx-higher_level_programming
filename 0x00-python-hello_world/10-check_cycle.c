#include "lists.h"

/**
 * check_cycle - checks for loops in LL
 * @list: head of linklist
 *
 * Description - check for loop in LL
 * Return: oneo if cycled, zeros if not
 */

int check_cycle(listint_t *list)
{
listint_t *slow, *fast;

if (!list)
{
return (0);
}
slow_l = list;
fast_o = list->next;
while (fast_o && slow_l && fast_o->next)
{
if (slow_l == fast_o)
{
return (1);
}
slow_l = slow_l->next;
fast_o = fast_o->next->next;
}
return (0);
}
