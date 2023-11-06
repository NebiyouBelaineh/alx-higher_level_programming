#include "lists.h"

/**
 * is_palindrome - checks a singly linked list if it is a palindrome or not
 * @head: pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *back = *head, *forward = *head, *current = *head, *middle = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		forward = forward->next->next;
		if (forward == NULL)
		{
			middle = back->next;
			break;
		}
		if (forward->next == NULL)
		{
			middle = back->next->next;
			break;
		}
	}
	reverse_list(&middle);

	while (middle != NULL && current != NULL)
	{
		if (middle->n == current->n)
		{
			middle = middle->next;
			current = current->next;
		}
		else
			return (0);
	}
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
