#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int amountDue = 50;
    int coin;

    while(amountDue > 0)
    {
        printf("Amount Due: %d\n", amountDue);
        printf("Insert Coin: ");
        scanf("%i", &coin);
        if((coin == 25) || (coin == 10) || (coin == 5))
        {
            amountDue = amountDue - coin;
        }
    }

    int changeOwed = abs(amountDue);
    printf("Change owed: %i\n", changeOwed);

}
