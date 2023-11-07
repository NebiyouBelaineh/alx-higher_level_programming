#include "lists.h"

/**
 * is_palindrome - checks a singly linked list if it is a palindrome or not
 * @head: pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *back = *head, *current = *head, *middle = *head;
	int index, count = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	current = *head;
	for (index = 0; index < (count / 2) - 1; index++)
		current = current->next;
	if ((count % 2) == 0 && current->n != current->next->n)
		return (0);

	current = current->next->next;
	reverse_list(&current);
	back = *head;
	middle = back;

	current = *head;
	while (back)
	{
		if (current->n != back->n)
			return (0);
		current = current->next;
		back = back->next;
	}
	reverse_list(&middle);
	return (1);
}
/**
* reverse_list - reverses a singly linked list
* @head: pointer to the head of the list
* Return: pointer to the head of the list
*/
void reverse_list(listint_t **head)
{
	listint_t *back = NULL;
	listint_t *current = *head;
	listint_t *forward = NULL;

	while (current)
	{
		forward = current->next;
		current->next = back;
		back = current;
		current = forward;
	}

	*head = back;
}
