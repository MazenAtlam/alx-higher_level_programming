#include "lists.h"

/**
 * is_palindrome - A function checks if a singly linked list is a palindrome
 * @head: The first element of the linked list
 *
 * Return: 0 (if it is not a palindrome), 1 (if it is a palindrome)
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	int arr[1024];
	int length = 0, i = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (curr != NULL)
	{
		length++;
		arr[i++] = curr->n;
		curr = curr->next;
	}
	for (i = 0, j = length - 1; i < length / 2; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
