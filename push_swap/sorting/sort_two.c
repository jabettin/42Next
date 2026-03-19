#include "../push_swap.h"

void	sort_two(t_node **a)
{
	if (!*a || !(*a)->next)
		return ;
	if ((*a)->value > (*a)->next->value)
		sa(a);
}