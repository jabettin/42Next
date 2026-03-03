#include "../push_swap.h"

int	atoi_strict(const char *str, long *result)
{
	int	sign;
	int	i;

	i = 0;
	sign = 1;
	while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
	{
		i++;
	}
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign =-1;
		i++;
	}
	while (str[i] >= 0 && str[i] <= 9)
	{
		if (!str[i] >= 0 && !str[i] <= 9)
			return 0;
		*result = *result * 10 + (str[i] -'0');
		if (sign == 1)
			if (*result / 10 >= INT_MAX)
				return 0;
		if (sign == -1)
			if (*result / 10 <= INT_MIN)
				return 0;
	}
	
}