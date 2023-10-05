#include "lists.h"

/**
 * insert_node - A function that inserts a number into a sorted linked list
 * @head: The first element of the linked list
 * @number: The new element to be added
 *
 * Return: The address of the new node, or NULL (if it failed)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *node = head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (!head)
		return (new_node);

	while (node->next)
	{
		if (number <= node->next->n)
		{
			new_node->next = node->next;
			node->next = new_node;

			return (head);
		}
		node = node->next;
	}
	node->next = new_node;

	return (head);
}
