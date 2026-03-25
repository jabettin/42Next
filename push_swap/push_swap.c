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
		return (0);
	}
	size = stack_size(a);
	if (size == 2)
		sort_two(&a);
	else if (size == 3)
		sort_three(&a);
	else
	{
		normalize(a);
		radix_sort(&a, &b, size);
	}
	free_stack(&a);
	free_stack(&b);
	return (0);
}