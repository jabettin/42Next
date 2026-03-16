#include "../push_swap.h"

void	pa(t_node **a, t_node **b)
{
	t_node	*temp;

	if (!*b)
		return ;
	temp = *b;
	*b = (*b)->next;
	temp->next = *a;
	*a = temp;
	write(1, "pa", 2);
	write(1, "\n", 1);
}