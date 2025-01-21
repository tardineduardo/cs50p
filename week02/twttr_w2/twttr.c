#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *input = malloc(100 * sizeof(char));
    char *output = malloc(100 * sizeof(char));

    printf("Input: ");
    fgets(input, 100, stdin);
    int n = strlen(input);

    for(int i = 0, j = 0; i < n + 1; i++)
    {
        if(!strchr("aeiouAEIOU", input[i]))
        {
            output[j] = input[i];
            j++;
        }

    }
    printf("Output: %s", output);
    free(output);
    free(input);
}



/*
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void)
{
    char *input = malloc(100);
    if (!input) return 1;

    printf("Input: ");
    fgets(input, 100, stdin);

    for (int i = 0, j = 0; input[i]; i++)
    {
        if (strchr("aeiouAEIOU", input[i]) == NULL)
        {
            input[j++] = input[i];
        }
    }
    printf("Output: %s", input);
    free(input);
}


*/
