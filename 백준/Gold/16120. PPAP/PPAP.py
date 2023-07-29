from collections import deque
import sys

print = sys.stdout.write

input = sys.stdin.readline
String = input()[:-1]

if String == "P":
    print("PPAP")

else:

    filterQueue = deque()
    processStack = deque()


    for i in range(len(String)):
        processStack.append(String[i])

    flag = False
    while len(processStack) != 0:
        currentChar = processStack.pop()
        filterQueue.append(currentChar)
        if len(filterQueue) >= 4:
            if filterQueue[-1] + filterQueue[-2] + filterQueue[-3] + filterQueue[-4] == "PPAP":
                for i in range(4):
                    filterQueue.pop()
                if len(processStack) == 0 and len(filterQueue) == 0:
                    flag = True
                    break
                processStack.append("P")

    if flag:
        print("PPAP")
    else:
        print("NP")