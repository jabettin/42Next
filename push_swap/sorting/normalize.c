/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   normalize.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/27 17:42:52 by jbetting          #+#    #+#             */
/*   Updated: 2026/03/27 17:45:31 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	normalize(t_node *a)
{
	t_node	*current;
	t_node	*scanner;
	int		rank;

	current = a;
	while (current != NULL)
	{
		rank = 0;
		scanner = a;
		while (scanner != NULL)
		{
			if (current->value > scanner->value)
				rank++;
			scanner = scanner->next;
		}
		current->value = rank;
		current = current->next;
	}
}
