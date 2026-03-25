#include "../push_swap.h"

int	atoi_strict(const char *str, long *result)
{
	int	sign;
	int	i;

	i = 0;
	sign = 1;
	*result = 0;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign =-1;
		i++;
	}
	if (!str[i])
		return (0);
	while (str[i] >= '0' && str[i] <= '9')
	{
		*result = *result * 10 + (str[i] -'0');
		if (*result > (long)INT_MAX + 1)
			return (0);
		i++;
	}
	if (str[i] != '\0')
		return (0);
	*result *= sign;
	if (*result > INT_MAX || *result < INT_MIN)
		return (0);
	return (1);
}