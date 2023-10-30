#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a singly linked list
 * @list: the head of the list to be checked
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *track1, *track2;

	if (list == NULL)
		return (0);

	track1 = list;
	track2 = list->next;

	while (track2 != NULL)
	{
		if (track1 == track2)
			return (1);
		track2 = track2->next;
	}
	return (0);
}
