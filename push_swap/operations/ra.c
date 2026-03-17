#include "../push_swap.h"

void	ra(t_node **a)
{
	t_node	*temp;
	t_node	*last;
	
	if (!*a || !(*a)->next)
		return ;
	temp = *a;
	*a = (*a)->next;
	last = *a;
	while (last->next)
		last = last->next;
	last->next = temp;
	temp->next = NULL;
	write(1, "ra", 2);
	write(1, "\n", 1);
}