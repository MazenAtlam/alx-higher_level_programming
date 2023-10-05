#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - A function that inserts a number into a sorted linked list
 * @head: The first element of the linked list
 * @number: The new element to be added
 *
 * Return: The address of the new node, or NULL (if it failed)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *node = *head;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (!(*head))
	{
		(*head) = new_node;

		return (new_node);
	}
	if (number <= (*head)->n)
	{
		new_node->next = (*head);

		return (new_node);
	}
	while (node->next)
	{
		if (number <= node->next->n)
		{
			new_node->next = node->next;
			node->next = new_node;

			return (new_node);
		}
		node = node->next;
	}
	node->next = new_node;

	return (new_node);
}
