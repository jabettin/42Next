/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   atoi_strict.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jbetting <jbetting@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/27 17:43:53 by jbetting          #+#    #+#             */
/*   Updated: 2026/03/27 18:12:21 by jbetting         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static int	parse_sign(const char *str, int *sign)
{
	if (str[0] == '-' || str[0] == '+')
	{
		if (str[0] == '-')
			*sign = -1;
		return (1);
	}
	return (0);
}

int	atoi_strict(const char *str, long *result)
{
	int	sign;
	int	i;

	sign = 1;
	*result = 0;
	i = parse_sign(str, &sign);
	if (!str[i])
		return (0);
	while (str[i] >= '0' && str[i] <= '9')
	{
		*result = *result * 10 + (str[i] - '0');
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
