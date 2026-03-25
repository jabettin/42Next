#include "../push_swap.h"

void	parse_args(int argc, char **argv, t_node **a)
{
	int		i;
	long	value;
	t_node	*new_node;

	i = 1;
	if (argc < 2)
		error_exit(a);
	while (i < argc)
	{
		if (!atoi_strict(argv[i], &value))
			error_exit(a);
		if (is_duplicate(*a, (int)value))
			error_exit(a);
		new_node = create_node((int)value);
		if(!new_node)
			error_exit(a);
		add_back(a, new_node);
		i++;
	}
		
}

void	error_exit(t_node **a)
{
	free_stack(a);
	write(2, "Error\n", 6);
	exit(1);
}