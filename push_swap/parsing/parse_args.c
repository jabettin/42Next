#include "../push_swap.h"

void	parse_args(int argc, char **argv, t_node **a)
{
	int	i;

	i = 0;
	if (argc < 1)
		error_exit(a);
	while (i < argc - 1)
	{
		
	}
		
}

void	error_exit(t_node **a)
{
	free_stack(a);
	write(2, "Error\n", 6);
	exit(1);
}