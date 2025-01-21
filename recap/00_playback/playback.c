#include <stdio.h>
#include <string.h>
#include <unistd.h>

int	main(void)
{
	int		len;
	char	string[5000];

	scanf("%[^\n]", string);
	len = strlen(string);
	for (int i = 0; i < len; i++)
	{
		if (string[i] == ' ')
			write(STDOUT_FILENO, "...", 3);
		else
			write(STDOUT_FILENO, &string[i], 1);
	}
	printf("\n");
	return (0);
}
