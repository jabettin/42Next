#include "../push_swap.h"

void	radix_sort(t_node **a, t_node **b, int size)
{
	int		tbits;
	int		bit;
	int		i;

	tbits = 0;
	bit = 0;
	while ((1 << tbits) <= size)
		tbits++;
	while (bit < tbits)
	{
		i = 0;
		while (i < size)
		{
			if (((*a)->value >> bit) & 1)
				ra(a);
			else
				pb(a, b);
			i++;
		}
		while (*b)
			pa(a, b);
		bit++;
	}
}