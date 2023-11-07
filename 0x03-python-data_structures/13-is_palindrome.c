#include "lists.h"

/**
 * is_palindrome - checks a singly linked list if it is a palindrome or not
 * @head: pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *back, *forward, *s_half, *f_half;

	back = *head;
	forward = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (forward != NULL && forward->next != NULL)
	{
		back = back->next;
		forward = forward->next->next;
	}
	f_half = reverse_list(&back);
	f_half = *head;

	while (s_half != NULL)
	{
		if (f_half->n != s_half->n)
			return (0);
		f_half = f_half->next;
		s_half = s_half->next;
	}
	return (1);
}
/**
* reverse_list - reverses a singly linked list
* @head: pointer to the head of the list
* Return: pointer to the head of the list
*/
listint_t *reverse_list(listint_t **head)
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
	return (*head);
}
