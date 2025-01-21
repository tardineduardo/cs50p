#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{
    char *input = malloc(50*sizeof(char));
    printf("camelCase: ");
    scanf("%s", input);
    char *output = malloc((strlen(input) + 1 ) * sizeof(char));
    int n = strlen(input);

    for(int i = 0, j = 0; i <= n; i++, j++)
    {
        if(isupper(input[i]))
        {
            output[j] = '_';
            output[j + 1] = input[i];
            output[j + 1] = tolower(output[j + 1]);
            n++;
            j++;
        }
        else if(islower(input[i]))
        {
            output[j] = input[i];
        }
    }

    printf("%s\n", output);
    free(output);
}
