#include "../push_swap.h"

void	sort_three(t_node **a)
{
	int	top;
	int	mid;
	int	bot;

	if (!*a || !(*a)->next || !(*a)->next->next)
		return ;
	top = (*a)->value;
	mid = (*a)->next->value;
	bot = (*a)->next->next->value;
	if (top < mid && mid < bot)
		return ;
	else if (top < bot && bot < mid)
	{
		rra(a);
		sa(a);
	}
	else if (mid < top && top < bot)
		sa(a);
	else if (bot < mid && mid < top)
	{
		sa(a);
		rra(a);
	}
	else if (mid < bot && bot < top)
		ra(a);
	else if (bot < top && top < mid)
		rra(a);
}