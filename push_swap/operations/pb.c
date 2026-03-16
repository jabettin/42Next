#include "../push_swap.h"

void	pb(t_node **a, t_node **b)
{
	t_node	*temp;

	if (!*a)
		return ;
	temp = *a;
	*a = (*a)->next;
	temp->next = *b;
	*b = temp;
	write(1, "pb", 2);	
	write(1, "\n", 1);
	
}