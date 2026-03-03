#include "../push_swap.h"

void	sa(t_node **stack)
{
	t_node	*first;
	t_node	*second;

	if (!stack || !*stack || !(*stack)->next)
		return;
	first = *stack;
	second = first->next;

	first->next = second->next;
	second->next = first;
	*stack = second;
}