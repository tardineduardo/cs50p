#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{
    char *input = malloc(50*sizeof(char));
    printf("camelCase: ");
    scanf("%s", input);


    for(int i = 0; i < strlen(input); i++)
    {
        if(isupper(input[i]))
        {
            int n = strlen(input);
            input[n + 1] = '_';
            for(int j = 0; j < n - i + 1; j++)
            {
                char temp = input[n + 1 - j];
                input[n + 1 - j] = input[n - j];
                input[n - j] = temp;
            }

            input[i+1] = tolower(input[i+1]);
        }
    }
    printf("%s\n", input);
}
