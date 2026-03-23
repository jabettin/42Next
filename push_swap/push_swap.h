/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/02 12:32:12 by jabettin          #+#    #+#             */
/*   Updated: 2026/03/23 14:13:46 by jbetting         ###   ########.fr       */
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

// stack
t_node	*create_node(int value);
void	add_back(t_node **stack, t_node *new_node);
void	free_stack(t_node **stack);
int		stack_size(t_node *stack);
int		is_sorted(t_node *stack);

// parsing
int		atoi_strict(const char *str, long *result);
int		is_duplicate(t_node *stack, int value);
void	parse_args(int argc, char **argv, t_node **a);
void	error_exit(t_node **a);

// operations
void	sa(t_node **stack);
void	pb(t_node **a, t_node **b);
void	pa(t_node **a, t_node **b);
void	ra(t_node **a);
void	rb(t_node **b);
void	rra(t_node **a);

// sorting
void	normalize(t_node *a, int size);
void	sort_two(t_node **a);
void	sort_three(t_node **a);
void	radix_sort(t_node **a, t_node **b, int size);
#endif