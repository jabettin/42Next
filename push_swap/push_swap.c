/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/27 17:43:33 by jbetting          #+#    #+#             */
/*   Updated: 2026/03/27 18:24:05 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	sort(t_node **a, t_node **b)
{
	int	size;

	if (is_sorted(*a))
	{
		free_stack(a);
		return ;
	}
	size = stack_size(*a);
	if (size == 2)
		sort_two(a);
	else if (size == 3)
		sort_three(a);
	else
	{
		normalize(*a);
		radix_sort(a, b, size);
	}
}

int	main(int argc, char **argv)
{
	t_node	*a;
	t_node	*b;

	a = NULL;
	b = NULL;
	if (argc == 1)
		return (0);
	parse_args(argc, argv, &a);
	sort(&a, &b);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
