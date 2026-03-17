/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/02 12:32:12 by jabettin          #+#    #+#             */
/*   Updated: 2026/03/17 20:40:57 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <unistd.h>
# include <limits.h>

typedef struct s_node
{
	int				value;
	struct	s_node	*next;
}	t_node;

t_node	*create_node(int value);
void	add_back(t_node **stack, t_node *new_node);
void	free_stack(t_node **stack);
int		stack_size(t_node *stack);
void	sa(t_node **stack);
void	pa(t_node **a, t_node **b);
void	pb(t_node **a, t_node **b);
void	ra(t_node **a);
void	rb(t_node **b);
void	rra(t_node **a);
int		atoi_strict(const char *str, long *result);
int		is_duplicate(t_node *stack, int value);
void	parse_args(int argc, char **argv, t_node **a);
int		is_sorted(t_node *stack);
#endif