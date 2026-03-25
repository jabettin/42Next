#include "../push_swap.h"

void	normalize(t_node *a)
{
	t_node	*current;
	t_node	*scanner;
	int		rank;

	current = a;
	while (current != NULL)
	{
		rank = 0;
		scanner = a;
		while (scanner != NULL)
		{
			if (scanner->value < current->value)
				rank++;
			scanner = scanner->next;
		}
		current->value = rank;
		current = current->next;
	}
}