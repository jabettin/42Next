#include "push_swap.h"

int	main(int argc, char **argv)
{
	t_node	*a;
	t_node	*b;
	int		size;

	a = NULL;
	b = NULL;
	if (argc == 1)
		return (0);
	parse_args(argc, argv, &a);
	if (is_sorted(a))
		{	
			free_stack(&a);
			return ;
		}
	size = stack_size(&a);
	
	free_stack(&a);
	free_stack(&b);
}