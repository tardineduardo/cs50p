#include <stdio.h>
#include <unistd.h>

int	ft_strlen(const char *s)
{
	int	a;

	if (!s)
		return (-1);

	a = 0;
	while (s[a] != '\0')
		a++;
	return (a);
}

void	ft_tolower(char *c)
{
	if (!c)
		return;

	if (*c >= 'A' && *c <= 'Z')
		*c += 32;
}


int	main(void)
{
	int		a;
	int		len;
	char	string[5000];

	scanf("%[^\n]", string);
	len = ft_strlen(string);

	a = 0;
	while (a < len)
		ft_tolower(&string[a++]);

	a = 0;
	while (a < len)
		write(STDOUT_FILENO, &string[a++], 1);

	write(STDOUT_FILENO, "\n", 1);
	return (0);
}
