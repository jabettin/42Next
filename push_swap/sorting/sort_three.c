/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_three.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/27 17:42:36 by jbetting          #+#    #+#             */
/*   Updated: 2026/03/27 18:06:42 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static void	operations(t_node **a, int top, int mid, int bot)
{
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
	operations(a, top, mid, bot);
}
