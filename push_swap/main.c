#include "push_swap.h"

int	main(int argc, char **argv)
{
	t_node	*a;
	t_node	*b;
	int		i;
	int		result;

	i = 0;
	b = NULL;
	if (argc == 1)
		return ;
	while (i < argc -1)
	{
		parse_args(argc, argv, &a);
		if (is_sorted(a))
		{
			free_stack(&a);
			return ;
		}
		result = stack_size(&a);
		if (result == )
		i++;
		
	}
	free_stack(&a);
}