#include "lists.h"

listint_t *find_middle(listint_t *head);
listint_t *reverse_list(listint_t *head);
int compare_lists(listint_t *head1, listint_t *head2);
int is_palindrome(listint_t **head);

/**
 * find_middle - Finds the middle node of a linked list
 * @head: The head of the linked list
 *
 * Return: The middle node of the list, or NULL if the list is empty
 */

listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
	slow = slow->next;
	fast = fast->next->next;
	}

	return (slow);
}

/**
 * reverse_list - Reverses a linked list
 * @head: The head of the list to be reversed
 *
 * Return: The head of the reversed list
 *
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * compare_lists - Compares two linked lists
 * @head1: The head of the first list
 * @head2: The head of the second list
 *
 * Return: 1 if the lists are identical, 0 otherwise.
 */

int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *tmp1 = head1;
	listint_t *tmp2 = head2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n != tmp2->n)
		{
			return (0);
		}
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}

	return (tmp1 == NULL && tmp2 == NULL);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: head The head of the list to check
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *mid;
	listint_t *rev;
	int res;

	if (*head == NULL)
	{
		return (1);
	}

	mid = find_middle(*head);
	rev = reverse_list(mid);

	res = compare_lists(*head, rev);

	rev = reverse_list(rev);

	return (res);
}
