#include "lists.h"

/**
 * is_palindrome - checks a singly linked list if it is a palindrome or not
 * @head: pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int index, count = 0, list_arr[1000];
	listint_t *current;

	current = *head;

	if (*head == NULL)
		return (1);
	for (index = 0; current != NULL; index++)
	{
		list_arr[index] = current->n;
		current = current->next;
		count++;
	}
	for (index = 0; index < floor(count / 2); index++)
	{
		if (list_arr[index] == list_arr[count - 1 - index])
			continue;
		else
			return (0);
	}
	return (1);

}
