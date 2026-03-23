#include "../push_swap.h"

void	rra(t_node **a)
{
	t_node	*last;
	t_node	*secondlast;

	if(!*a || !(*a)->next)
		return ;
	secondlast = *a;
	while (secondlast->next->next != NULL)
		secondlast = secondlast->next;
	last = secondlast->next;
	secondlast->next = NULL;
	last->next = *a;
	*a = last;
	write(1, "rra", 3);
	write(1, "\n", 1);
	

}