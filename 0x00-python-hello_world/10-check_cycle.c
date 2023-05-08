#include "lists.h"
/**
 * check_cycle - checks if a linked list is circular or not
 *
 * @list: linked list to check
 *
 * Return: 1 (linked list is circular) 0 (no loop detected)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = NULL, *fast_ptr = NULL;

	slow_ptr = fast_ptr = list;
	while (list && slow_ptr && fast_ptr && slow_ptr->next && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr || !slow_ptr)
			return (0);
		if (fast_ptr->next == slow_ptr)
			return (1); /* loop found */
	}
	/* no loop detected */
	return (0);
}
