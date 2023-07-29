import sys
from collections import deque

input = sys.stdin.readline
notation =input()
notation = notation[:-1]

operators = deque()
results = deque()

for i in range(len(notation)):
    character = notation[i]
    
    if character == "*" or character == "/":
        if len(operators) == 0:
            operators.append(character)
            continue
        if operators[-1] == "+" or operators[-1] == "-" or operators[-1] == "(":
            operators.append(character)
        elif operators[-1] == "*" or operators[-1] == "/":
            results.append(operators.pop())
            operators.append(character)
        else:
            num = len(operators)
            for j in range(num):
                if operators[num - 1 - j] == "(":
                    break
                else:
                    results.append(operators.pop())
            operators.append(character)
    elif character == "+" or character == "-":
        if len(operators) == 0:
            operators.append(character)
            continue
        if operators[-1] == "(":
            operators.append(character)
        else:
            num = len(operators)
            for j in range(num):
                if operators[num - 1 - j] == "(":
                    break
                else:
                    results.append(operators.pop())
            operators.append(character)
    elif character == "(":
        operators.append(character)
    elif character == ")":
        num = len(operators)
        for j in range(num):
            if operators[num - 1 - j] == "(":
                operators.pop()
                break
            else:
                results.append(operators.pop())
    else:
        results.append(character)

if len(operators) != 0:
    for i in range(len(operators)):
        results.append(operators.pop())
answer = ""             
for i in range(len(results)):
    answer += results[i]

print(answer)