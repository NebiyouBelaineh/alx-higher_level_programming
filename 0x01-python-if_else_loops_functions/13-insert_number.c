#include "lists.h"
#include <stdlib.h>
listint_t *insert_negative(listint_t **head, int number);
/**
 * insert_node - inserts a node with a value in a sorted singly linked list
 * @head: address of the head of the list
 * @number: integer value that the node should have
 * Return: address of the new node inserted or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *current, *new_node;

	current = *head;

	if (head == NULL || *head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	/*if number is less than first node*/
	if (current == NULL || current->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	/*if number ranges between 2nd to last node*/
	while (current->next != NULL)
	{
		if ((current->next)->n >= number)
		{
			temp = current->next;
			current->next = new_node;
			new_node->next = temp;
			return (new_node);
		}
		current = current->next;
	}
	/*if number is greater than all nodes*/
	new_node->next = NULL;
	current->next = new_node;
	return (new_node);
}

