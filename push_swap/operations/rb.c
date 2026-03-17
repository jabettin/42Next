#include "../push_swap.h"

void	rb(t_node **b)
{
	t_node	*temp;
	t_node	*last;

	if (!*b || !(*b)->next)
		return ;
	temp = *b;
	*b = (*b)->next;
	last = *b;
	while (last->next)
		*b = (*b)->next;
	last->next = temp;
	temp->next = NULL;
	write(1, "rb", 2);
	write(1, "\n", 1);
}