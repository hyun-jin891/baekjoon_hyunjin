import sys
import heapq

input = sys.stdin.readline
N = int(input()[:-1])
preQ = []


for i in range(N):
    deadline, cupNoodle = map(int, input().split())
    preQ.append((deadline, cupNoodle))
    
heapq.heapify(preQ)
solvedQ = []
heapq.heapify(solvedQ)


while len(preQ) != 0:
    currentDeadline, currentNoodle = heapq.heappop(preQ)
    if len(solvedQ) < currentDeadline:
        heapq.heappush(solvedQ, (currentNoodle, currentDeadline))

    else:
        compareNoodle, compareDeadline = heapq.heappop(solvedQ)
        if currentNoodle > compareNoodle:
            heapq.heappush(solvedQ, (currentNoodle, currentDeadline))
        else:
            heapq.heappush(solvedQ, (compareNoodle, compareDeadline))

result = 0
while len(solvedQ) != 0:
    solvedNoodle = heapq.heappop(solvedQ)[0]
    result += solvedNoodle

print(result)