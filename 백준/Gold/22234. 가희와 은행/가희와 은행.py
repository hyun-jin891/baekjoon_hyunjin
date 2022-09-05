from collections import deque
import sys

def heapSort(a1, a2, a3):
    for i in range(len(a3)):
        c = i
        while c != 0:
            r = (c - 1)//2
            if a3[r] < a3[c]:
                a1[r], a1[c] = a1[c], a1[r]
                a2[r], a2[c] = a2[c], a2[r]
                a3[r], a3[c] = a3[c], a3[r]
            c = r
    for j in range(len(a3) - 1, -1, -1):
        a1[0], a1[j] = a1[j], a1[0]
        a2[0], a2[j] = a2[j], a2[0]
        a3[0], a3[j] = a3[j], a3[0]
        r = 0
        c = 1
        
        while c < j:
            c = 2 * r + 1
            if c < j - 1 and a3[c] < a3[c + 1]:
                c += 1
            if c < j and a3[r] < a3[c]:
                a1[r], a1[c] = a1[c], a1[r]
                a2[r], a2[c] = a2[c], a2[r]
                a3[r], a3[c] = a3[c], a3[r]
            r = c

input = sys.stdin.readline

N, T, W = map(int, input().split())

ids = [0]
times = [0]
cs = [0]

for i in range(1, N + 1):
    ID, Time = map(int, input().split())
    ids.append(ID)
    times.append(Time)
    cs.append(0)

M = int(input())
extraID = []
extraTime = []
extraCs = []

for i in range(N + 1, N + M + 1):
    ID, Time, Cs = map(int, input().split())
    extraID.append(ID)
    extraTime.append(Time)
    extraCs.append(Cs)

heapSort(extraID, extraTime, extraCs)
ids.extend(extraID)
times.extend(extraTime)
cs.extend(extraCs)

currentTime = 0
waitList = deque([i for i in range(1, N + 1)])
minIndexForCx = N + 1
flag = True

while (flag):
    processingNumber = waitList.popleft()
    processingId = ids[processingNumber]
    processingTime = times[processingNumber]
    
    if processingTime > T:
        for i in range(T):
            sys.stdout.write(str(processingId) + "\n")
            currentTime += 1
            
            if currentTime == W:
                flag = False
                break

            if minIndexForCx <= N + M and currentTime == cs[minIndexForCx]:
                waitList.append(minIndexForCx)
                minIndexForCx += 1
                
        times[processingNumber] -= T
        waitList.append(processingNumber)
    else:
        for i in range(processingTime):
            sys.stdout.write(str(processingId) + "\n")
            currentTime += 1
            
            if currentTime == W:
                flag = False
                break

            if minIndexForCx <= N + M and currentTime == cs[minIndexForCx]:
                waitList.append(minIndexForCx)
                minIndexForCx += 1
        times[processingNumber] = 0