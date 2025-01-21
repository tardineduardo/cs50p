#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <readline/readline.h>

bool	is_vowel(char c)
{
	c = tolower(c);
	if (c == 'a' ||
		c == 'e' ||
		c == 'i' ||
		c == 'o' ||
		c == 'u')
		return (true);
	return(false);
}

int	main(void)
{
	char	*input;
	char	*output;
	int		len;
	int		a;
	int		b;

	input = readline("Input: ");
	len = strlen(input);
	output = calloc(len, sizeof(char));

	a = 0;
	b = 0;
	while (a < len)
	{
		if (!is_vowel(input[a]))
			output[b++] = input[a++];
		else
			a++;
	}
	printf("Output: %s\n", output);
	free(output);
	free(input);
	return (0);
}
