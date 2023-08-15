#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome -checks if a singly linked list is a palindrome
 * @head: pointeri
 * Return: 1 if palindrom,0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int list[2000];
	int i, j;
	listint_t *p = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	i = 0;
	while (p)
	{
		list[i] = p->n;
		p = p->next;
		i++;
	}
	i = i - 1;
	for (j = 0; i > j; i--, j++)
	{
		if (list[j] != list[i])
			return (0);
	}
	return (1);
}
