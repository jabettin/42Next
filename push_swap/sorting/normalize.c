#include "../push_swap.h"

static void	sort_array(int *arr, int size)
{
	int	i;
	int	j;
	int	temp;

	i = 0;
	while (i < size - 1)
	{
		j = i + 1;
		while (j < size)
		{
			if (arr[i] > arr[j])
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
			j++;
		}
		i++;
	}
}

static void	fill_sorted(t_node *a, int *sorted, int size)
{
	t_node	*temp;
	int		i;

	temp = a;
	i = 0;
	while (temp)
	{
		sorted[i] = temp->value;
		temp = temp->next;
		i++;
	}
	sort_array(sorted, size);
}

void	normalize(t_node *a, int size)
{
	int		*sorted;
	t_node	*temp;
	int		i;

	sorted = malloc(sizeof(int) * size);
	if (!sorted)
		return ;
	fill_sorted(a, sorted, size);
	temp = a;
	while (temp)
	{
		i = 0;
		while (i < size)
		{
			if (temp->value == sorted[i])
			{
				temp->value = i;
				break ;
			}
			i++;
		}
		temp = temp->next;
	}
	free(sorted);
}