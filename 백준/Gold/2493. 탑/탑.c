#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct node
{
  int index;
  int data;
} Node;

Node* createNode(int index ,int data)
{
  Node* newNode = (Node*)malloc(sizeof(Node));
  newNode->data = data;
  newNode->index = index;

  return newNode;
}

void destroyNode(Node** node)
{
  free(*node);
  *node = NULL;
}

typedef struct stack
{
  int capacity;
  int top;

  Node** nodeList;
} Stack;

void createStack(Stack** stack, int capacity)
{
  *stack = (Stack*)malloc(sizeof(Stack));
  (*stack)->capacity = capacity;
  (*stack)->top = -1;
  (*stack)->nodeList = (Node**)malloc(sizeof(Node*) * capacity);
}

int isEmpty(Stack* stack)
{
  return (stack->top == -1);
}

void push(Stack* stack, Node* node)
{
  stack->top++;
  stack->nodeList[stack->top] = node;
}

Node* pop(Stack* stack)
{
  Node* poped = stack->nodeList[stack->top--];
  return poped;
}

Node* getTop(Stack* stack)
{
  return stack->nodeList[stack->top];
}

void destroyStack(Stack** stack)
{
  free((*stack)->nodeList);
  (*stack)->nodeList = NULL;
  free(*stack);
  *stack = NULL;
}


int main()
{
    Stack* stack = NULL;
    Stack* tempStack = NULL;

    int N = 0;

    scanf("%d", &N);

    int* result = (int*)malloc(sizeof(int) * N);
    memset(result, 0, sizeof(int) * N);


    createStack(&stack, N+1);
    createStack(&tempStack, N+1);

    for (int i = 0; i < N; i++)
    {
      int temp = 0;
      scanf("%d", &temp);
      Node* newNode = createNode(i + 1, temp);
      push(stack, newNode);
    }

    push(tempStack, pop(stack));

    while (!isEmpty(stack))
    {
      Node* compareElement = pop(stack);

      while (!isEmpty(tempStack) && compareElement->data > getTop(tempStack)->data)
      {
        Node* poped = pop(tempStack);
        result[poped->index - 1] = compareElement->index;
      }
      push(tempStack, compareElement);
    }

    
    for (int i = 0; i < N; i++)
    {
      if (i == N-1)
      {
        printf("%d", result[i]);  
      }
      else
      {       
        printf("%d ", result[i]);
      }

    }

    destroyStack(&stack);
    destroyStack(&tempStack);
    free(result);
    result = NULL;

}