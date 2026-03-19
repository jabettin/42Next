#include "../push_swap.h"

void	normalize(t_node *a, int size)
{
	t_node	*temp;
	int		min;
	int		i;

	i = 0;
	while (i < size)
	{
		min = find_min(a);
		temp = a;
		while (temp)
		{
			if (temp->value == min)
			{
				temp->value = i;
				break ;
			}
			temp = temp->next;
		}
		i++;
	}
}

int	find_min(t_node *a)
{
	int	min;

	min = a->value;
	while (a)
	{
		if (a->value < min)
			min = a->value;
		a = a->next;
	}
	return (min);
}