#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

bool start(char *plate);
bool size(char *plate);
bool numbers(char *plate);
bool zero(char *plate);
bool specialchars(char *plate);

int main(void)
{
    char *plate = calloc(7, sizeof(char));
    printf("Plate: ");
    scanf("%6s", plate);

    if (start(plate) && size(plate) && numbers(plate) && zero(plate) && specialchars(plate))
        printf("Valid\n");
    else
        printf("Invalid\n");

    free(plate);
}

bool isvalid(char *plate)
{



}



bool start(char *plate)
{
    if ((isalpha(plate[0])) && (isalpha(plate[1])))
        return true;
    else
        return false;
}

bool size(char *plate)
{
    if((strlen(plate) >= 2) && (strlen(plate) <= 6))
        return true;
    else
        return false;
}

bool numbers(char *plate)
{
    for(int i = 0; i < strlen(plate); i++)
        if(isdigit(plate[i]) && isalpha(plate[i + 1]))
            return false;
    return true;
}

bool zero(char *plate)
{
    for(int i = 2; i < strlen(plate); i++)
        if(isalpha(plate[i - 1]) && (plate[i] == '0'))
            return false;
    return true;
}

bool specialchars(char *plate)
{
    for(int i = 0; i < strlen(plate); i++)
        if(!isalnum(plate[i]))
            return false;
    return true;
}
