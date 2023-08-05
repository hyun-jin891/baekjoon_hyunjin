from collections import deque
import sys

input = sys.stdin.readline

DayNum = int(input()[:-1])
wageList = input()[:-1].split()
wageList = list(map(int, wageList))
wageList.append(0)

wageStack = deque()
maximumArea = 0

for i in range(len(wageList)):
    currentWage = wageList[i]
    
    if len(wageStack) == 0:
        wageStack.append((i, currentWage))
        continue
    
    if currentWage < wageStack[-1][1]:
        index = 0
        while len(wageStack) != 0 and currentWage < wageStack[-1][1]:
            index, wage = wageStack.pop()
            if maximumArea < (i - index) * wage:
                maximumArea = (i - index) * wage
        wageStack.append((index, currentWage))
    else:
        wageStack.append((i, currentWage))


print(maximumArea)