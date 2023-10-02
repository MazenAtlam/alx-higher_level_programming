#include "lists.h"

/**
 * check_cycle - A function that checks if there is a cycle in a linked list
 * @list: The head of the linked list
 *
 * Return: 1 (if there is a cycle), 0 (if there isn't any cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *hear = list;
	listint_t *turtoise = list;

	if (!list)
		return (0);

	while (hear && hear->next && turtoise)
	{
		turtoise = turtoise->next;
		hear = hear->next->next;
		if (hear == turtoise)
			return (1);
	}
	return (0);
}
