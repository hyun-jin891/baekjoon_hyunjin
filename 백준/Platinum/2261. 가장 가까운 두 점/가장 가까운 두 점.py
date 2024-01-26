import sys
input = sys.stdin.readline
print = sys.stdout.write
def calDistance(start, end):                               
    minDistance = ((data[0][0] - data[1][0]) ** 2 + (data[0][1] - data[1][1]) ** 2)
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            d = ((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2)
            if minDistance > d:
                minDistance = d

    
    return minDistance
        

def func(start, end):
    if end - start <= 2:
        minDistance = calDistance(start, end)
        return minDistance
    
    mid = (start + end) // 2
    midLine_x = data[mid][0]
    
    
    left_min = func(start, mid)
    minDistance = left_min
    right_min = func(mid + 1, end)
    
    if left_min <= right_min:
        minDistance = left_min
    else:
        minDistance = right_min
    
    newCoordinateList = []
    for i in range(start, end + 1):
        if midLine_x - (minDistance) ** 0.5 <= data[i][0] <= midLine_x + (minDistance) ** 0.5:
            newCoordinateList.append(data[i])
    newCoordinateList.sort(key=lambda x : x[1])
    
    for i in range(len(newCoordinateList) - 1):
        for j in range(i + 1, len(newCoordinateList)):
            if (newCoordinateList[j][1] - newCoordinateList[i][1]) ** 2 >= minDistance:
                break
            currentDistance = (newCoordinateList[j][0] - newCoordinateList[i][0]) ** 2 + (newCoordinateList[j][1] - newCoordinateList[i][1]) ** 2
            if currentDistance < minDistance:
                minDistance = currentDistance
    #intermediateCoordinateList1 = []
    #intermediateCoordinateList2 = []

    #for i in range(mid):
     #   if midLine_x - (minDistance) ** 0.5 <= data[i][0]:
      #      intermediateCoordinateList1.append(data[i])

    
    #for i in range(mid, len(data)):
     #   if data[i][0] <= midLine_x + (minDistance) ** 0.5:
      #      intermediateCoordinateList2.append(data[i])
    #intermediateCoordinateList2.sort(key=lambda x : x[1])
    #newCoordinateList = intermediateCoordinateList1 + intermediateCoordinateList2
        
    return minDistance   
    
N = int(input())

data = []

for i in range(N):
    x, y = map(int, input().split())
    data.append([x, y])

data.sort(key=lambda x : x[0])

print(str(func(0, len(data) - 1)))