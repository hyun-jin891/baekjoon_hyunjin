string = input()
boom = input()
boom_l = []
for i in range(len(boom)):
    boom_l.append(boom[len(boom) - i - 1])
stack = []

for i in range(len(string)):
    stack.append(string[len(string) - 1 - i])
    if len(stack) >= len(boom) and string[len(string) - 1 - i] == boom[0]:
        if stack[len(stack) - len(boom) : len(stack)] == boom_l:
            for i in range(len(boom)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    for i in range(len(stack)):
        print(stack.pop(), end='')