#include "lists.h"

/**
 * is_palindrome - checks a singly linked list if it is a palindrome or not
 * @head: pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int index, count = 0, *list_arr;
	listint_t *current;

	current = *head;

	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	current = *head;

	list_arr = malloc(sizeof(int) * count);

	for (index = 0; index < count && current != NULL; index++)
	{
		list_arr[index] = current->n;
		current = current->next;
	}
	for (index = 0; index < floor(count / 2); index++)
	{
		if (list_arr[index] == list_arr[count - 1 - index])
			continue;
		else
		{
			free(list_arr);
			return (0);
		}
	}
	free(list_arr);
	return (1);

}
