#include "../push_swap.h"
#include "../libft/libft.h"

static void	free_split(char **split)
{
	int	i;

	i = 0;
	while (split[i])
		free(split[i++]);
	free(split);
}

static void	parse_str(char *str, t_node **a, char **split)
{
	long	value;
	t_node	*new_node;

	if (!atoi_strict(str, &value))
	{
		free_split(split);
		error_exit(a);
	}
	if (is_duplicate(*a, (int)value))
	{
		free_split(split);
		error_exit(a);
	}
	new_node = create_node((int)value);
	if (!new_node)
	{
		free_split(split);
		error_exit(a);
	}
	add_back(a, new_node);
}

static void	parse_split(char *str, t_node **a)
{
	char	**split;
	int		i;

	split = ft_split(str, ' ');
	if (!split)
		error_exit(a);
	i = 0;
	while (split[i])
	{
		parse_str(split[i], a, split);
		i++;
	}
	free_split(split);
}

void	parse_args(int argc, char **argv, t_node **a)
{
	int		i;
	long	value;
	t_node	*new_node;

	if (argc < 2)
		error_exit(a);
	if (argc == 2)
	{
		parse_split(argv[1], a);
		return ;
	}
	i = 1;
	while (i < argc)
	{
		if (!atoi_strict(argv[i], &value))
			error_exit(a);
		if (is_duplicate(*a, (int)value))
			error_exit(a);
		new_node = create_node((int)value);
		if (!new_node)
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