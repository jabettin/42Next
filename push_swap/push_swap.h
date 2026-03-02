/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jabettin <jabettin@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/02 12:32:12 by jabettin          #+#    #+#             */
/*   Updated: 2026/03/02 13:46:04 by jabettin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
#include <unistd.h>

typedef struct s_node
{
	int				value;
	struct	s_node	*next;
}	t_node;

t_node	*create_node(int value);
void	add_back(t_node **stack, t_node *new_node);
void	free_stack(t_node **stack);
int		stack_size(t_node *stack);
#endif