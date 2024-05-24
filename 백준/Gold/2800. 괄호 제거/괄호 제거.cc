#include <stdio.h>
#include <malloc.h>
#include <cstring>
#include <math.h>
#include <stdlib.h>

typedef struct stack
{
    int Capacity;
    int Top;
    char* data;
} Stack;

typedef struct stack2
{
    int Capacity;
    int Top;
    int* data;
} Stack2;

void createStack(Stack** charStack, int capacity)
{
    *charStack = (Stack*)malloc(sizeof(Stack));
    (*charStack)->data = (char*)malloc(sizeof(char) * (capacity + 1));
    (*charStack)->Capacity = capacity;
    (*charStack)->Top = -1;
    
}

void createStack2(Stack2** intStack, int capacity)
{
    *intStack = (Stack2*)malloc(sizeof(Stack2));
    (*intStack)->data = (int*)malloc(sizeof(int) * (capacity + 1));
    (*intStack)->Capacity = capacity;
    (*intStack)->Top = -1;
}

void deleteStack(Stack** charStack)
{
    free((*charStack)->data);
    (*charStack)->data = NULL;
    free(*charStack);
    *charStack = NULL;
}

void deleteStack2(Stack2** intStack)
{
    free((*intStack)->data);
    (*intStack)->data = NULL;
    free(*intStack);
    *intStack = NULL;
}

void push(Stack* charStack, char datum)
{
    charStack->Top++;
    charStack->data[charStack->Top] = datum;
}

void push2(Stack2* intStack, int datum)
{
    intStack->Top++;
    intStack->data[intStack->Top] = datum;
}

char pop(Stack* charStack)
{
    char topDatum = charStack->data[charStack->Top];
    charStack->Top--;

    return topDatum;
}

int pop2(Stack2* intStack)
{
    int topDatum = intStack->data[intStack->Top];
    intStack->Top--;

    return topDatum;
}

int countParenthesis(char* data)
{
    int count = 0;

    for (int i = 0; i < strlen(data); i++)
    {
        char datum = data[i];
        if (datum == '(')
            count++;
    }

    return count;
}

void show(char** array, int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%s\n", array[i]);
    }

}

int compare(const void* a, const void* b)
{
    return strcmp(*(char**)a, *(char**) b);
}



int main()
{
    char notation[201];
    memset(notation, 0, sizeof(notation));
    Stack* operatorStack = NULL;
    Stack2* parenthesisStack = NULL;
    

    scanf("%s", notation);

    int length = strlen(notation);
    int n = countParenthesis(notation);
    createStack(&operatorStack, length);
    createStack2(&parenthesisStack, 11);

    int sizeofArray = pow(2, n);

    char** resultArray = (char**)malloc(sizeof(char*) * sizeofArray);
    for (int i = 0; i < sizeofArray; i++)
    {
        resultArray[i] = (char*)malloc(sizeof(char) * 201);
    }

    int lengthResult = 0;

    for (int i = 1; i < pow(2, n); i++)
    {
        char resultString[201];
        memset(resultString, 0, sizeof(resultString));
        int numberLeftParenthesis = 0;
        int numberRightParenthesis = 0;

        for (int j = 0; j < strlen(notation); j++)
        {
            char currentChar = notation[j];
            if (currentChar == '(')
            {
                numberLeftParenthesis++;
                push2(parenthesisStack, numberLeftParenthesis);
                if (i & (1 << (n - numberLeftParenthesis)))
                {
                    continue;
                }
                else
                {
                    push(operatorStack, currentChar);
                }
            }
            else if (currentChar == ')')
            {
                numberRightParenthesis = pop2(parenthesisStack);
                         
                if (i & (1 << n - numberRightParenthesis))
                {
                    continue;
                }
                else
                {
                    push(operatorStack, currentChar);
                }
            }
            else
            {
                push(operatorStack, currentChar);
            }
        }

        int resultLength = operatorStack->Top;
        for (int k = 0; k < resultLength + 1; k++)
        {
            resultString[resultLength - k] = pop(operatorStack);
        }

        strcpy(resultArray[lengthResult], resultString);
        lengthResult++;

    }

    qsort(resultArray, lengthResult, sizeof(char*), compare);


    for (int i = 0; i < lengthResult; i++)
    {
        if (i >= 1 && strcmp(resultArray[i-1], resultArray[i]) == 0)
            continue;
        else
        {
            printf("%s\n", resultArray[i]);
        }
    }



    deleteStack(&operatorStack);
    deleteStack2(&parenthesisStack);
    for (int i = 0; i < sizeofArray; i++)
    {
        free(resultArray[i]);
        resultArray[i] = NULL;
    }
    free(resultArray);
    *resultArray = NULL;

    return 0;
}