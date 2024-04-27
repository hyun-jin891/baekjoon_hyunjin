#include <stdio.h>
#include <stdlib.h>

typedef struct Worm
{
    long size;
    long location;
    struct Worm* NextWorm;
    struct Worm* preWorm;
}worm;

worm* createWorm(long size, long location)
{
    worm* oneWorm = (worm*)malloc(sizeof(worm));
    oneWorm->size = size;
    oneWorm->location = location;
    oneWorm->NextWorm = NULL;
    oneWorm->preWorm = NULL;

    return oneWorm;
}

void destroyWorm(worm** target)
{
    free(*target);
    *target = NULL;
}


void appendWorm(worm** firstWorm, worm* newWorm)
{
    if (*firstWorm == NULL)
    {
        *firstWorm = newWorm;
        (*firstWorm)->NextWorm = *firstWorm;
        (*firstWorm)->preWorm = *firstWorm;
    }
    else
    {
        worm* tailWorm = (*firstWorm)->preWorm;        
        newWorm->preWorm = tailWorm;
        newWorm->NextWorm = tailWorm->NextWorm;
        tailWorm->NextWorm = newWorm;
        (*firstWorm)->preWorm = newWorm;
    }
}

void deleteWorm(worm** firstWorm, worm* target)
{
    if (*firstWorm == target)
    {
        (*firstWorm)->preWorm->NextWorm = (*firstWorm)->NextWorm;
        (*firstWorm)->NextWorm->preWorm = (*firstWorm)->preWorm;
        (*firstWorm) = (*firstWorm)->NextWorm;

        target->preWorm = NULL;
        target->NextWorm = NULL;
    }
    else
    {
        target->preWorm->NextWorm = target->NextWorm;
        target->NextWorm->preWorm = target->preWorm;

        target->NextWorm = NULL;
        target->preWorm = NULL;
    }
}



int main()
{
    long n = 0;
    worm* wormList = NULL;

    scanf("%ld", &n);

    for (int i = 0; i < n; i++)
    {
        long temp = 0;
        scanf("%ld", &temp);
        worm* oneWorm = createWorm(temp, i + 1);
        appendWorm(&wormList, oneWorm);
    }

    long deleteNum = 0;
    worm* currentWorm = wormList;

    while (deleteNum != n - 1)
    {
        long addSize = 0;
        if (currentWorm->NextWorm != wormList)
        {
            if (currentWorm->size >= currentWorm->NextWorm->size)
            {
                addSize = addSize + currentWorm->NextWorm->size;
                worm* temp = currentWorm->NextWorm;
                deleteWorm(&wormList, currentWorm->NextWorm);
                destroyWorm(&temp);
                deleteNum++;
            }
        }

        if (currentWorm != wormList)
        {
            if (currentWorm->size >= currentWorm->preWorm->size)
            {
                addSize = addSize + currentWorm->preWorm->size;
                worm* temp = currentWorm->preWorm;
                deleteWorm(&wormList, currentWorm->preWorm);
                destroyWorm(&temp);
                deleteNum++;
            }
        }

        currentWorm->size = currentWorm->size + addSize;

        currentWorm = currentWorm->NextWorm;

    }

    printf("%ld\n", wormList->size);
    printf("%ld\n", wormList->location);

    destroyWorm(&wormList);


    return 0;
}