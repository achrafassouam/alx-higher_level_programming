#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list contains a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 if not.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
