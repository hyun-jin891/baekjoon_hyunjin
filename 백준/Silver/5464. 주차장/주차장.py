from collections import deque


N, M = map(int, input().split())

RsList = [0]
for i in range(N):
    RsList.append(int(input()))
    
WkList = [0]
for i in range(M):
    WkList.append(int(input()))

priceSum = 0
emptySpaceList = [0] * (N + 1)
emptySpaceList[0] = -1
spaceOfCars = [0] * (M + 1)
waitCars = deque()

for i in range(2 * M):
    operation = int(input())
    if operation > 0:
        if 0 not in emptySpaceList:
            waitCars.append(operation)
        else:
            Index = emptySpaceList.index(0)
            priceSum += WkList[operation] * RsList[Index]
            spaceOfCars[operation] = Index
            emptySpaceList[Index] = 1
    else: 
        if len(waitCars) == 0:
            emptySpaceList[spaceOfCars[-operation]] = 0
            continue
        else:
            waitedCar = waitCars.popleft() 
            priceSum += WkList[waitedCar] * RsList[spaceOfCars[-operation]]
            spaceOfCars[waitedCar] = spaceOfCars[-operation]
            
            
print(priceSum) 