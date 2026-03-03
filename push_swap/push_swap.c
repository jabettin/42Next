#include "push_swap.h"
#include <stdio.h>

int main(void)
{
	t_node	*a = NULL;
	add_back(&a, create_node(3));
	add_back(&a, create_node(7));
	add_back(&a, create_node(1));

	printf("size: %d\n", stack_size(a));

	t_node	*temp = a;
	sa(&temp);
	while (temp)
	{
		printf("%d ", temp->value);
		temp = temp->next;
	}
	printf("\n");
	free_stack(&a);
	return 0;
}