#include <stdio.h>

int	main(void)
{
	int		price;
	int		paid;
	int		coin;

	price = 50;
	paid = 0;
	while (paid < price)
	{
		printf("Amount Due: %i\n", price - paid);
		printf("Insert coin: ");			
		if (scanf("%i", &coin) != 1)
		{
			printf("Invalid input. Please insert a valid coin.\n");
			while (getchar() != '\n');
			continue;
		}
		if (coin == 25 || coin == 10 || coin == 5)
			paid += coin;
		while (getchar() != '\n');
	}
	printf("Change Owed: %i\n", paid - price);
}
