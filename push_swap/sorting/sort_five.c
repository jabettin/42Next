/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_five.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/27 21:20:06 by jbetting          #+#    #+#             */
/*   Updated: 2026/03/27 21:20:13 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static int	find_min_pos(t_node *a)
{
	t_node	*temp;
	int		min_val;
	int		min_pos;
	int		i;

	temp = a;
	min_val = temp->value;
	min_pos = 0;
	i = 0;
	while (temp)
	{
		if (temp->value < min_val)
		{
			min_val = temp->value;
			min_pos = i;
		}
		temp = temp->next;
		i++;
	}
	return (min_pos);
}

static void	push_min(t_node **a, t_node **b, int size)
{
	int	pos;

	pos = find_min_pos(*a);
	if (pos <= size / 2)
	{
		while (pos-- > 0)
			ra(a);
	}
	else
	{
		while (pos++ < size)
			rra(a);
	}
	pb(a, b);
}

void	sort_five(t_node **a, t_node **b, int size)
{
	push_min(a, b, size);
	push_min(a, b, size - 1);
	sort_three(a);
	pa(a, b);
	pa(a, b);
}
