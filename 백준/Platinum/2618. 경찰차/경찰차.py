import sys
input = sys.stdin.readline

N = int(input())
case = int(input())

police1Coordinate = [[1, 1]]
police2Coordinate = [[N, N]]


for i in range(case):
    x, y = input().split()
    coordinate = []
    coordinate.append(int(x))
    coordinate.append(int(y))
    police1Coordinate.append(coordinate)
    police2Coordinate.append(coordinate)
    
dp = [[0] * len(police1Coordinate) for i in range(len(police1Coordinate))]
tracking = [[""] * len(police1Coordinate) for i in range(len(police1Coordinate))]

for i in range(len(police1Coordinate)):
    for j in range(len(police2Coordinate)):
        if i == j:
            dp[j][i] = 0
            
        elif i - j == 1:
            minDistance = dp[j][0] + abs(police1Coordinate[i][0] - police1Coordinate[0][0]) + abs(police1Coordinate[i][1] - police1Coordinate[0][1])
            minIndex = 0
            for k in range(1, i - 1):
                Distance = dp[j][k] + abs(police1Coordinate[i][0] - police1Coordinate[k][0]) + abs(police1Coordinate[i][1] - police1Coordinate[k][1])
                if Distance < minDistance:
                    minDistance = Distance
                    minIndex = k
            dp[j][i] = minDistance
            tracking[j][i] = minIndex

        
        elif j - i == 1:
            minDistance = dp[0][i] + abs(police2Coordinate[j][0] - police2Coordinate[0][0]) + abs(police2Coordinate[j][1] - police2Coordinate[0][1])
            minIndex = 0
            for k in range(1, j - 1):
                Distance = dp[k][i] + abs(police2Coordinate[j][0] - police2Coordinate[k][0]) + abs(police2Coordinate[j][1] - police2Coordinate[k][1])
                if Distance < minDistance:
                    minDistance = Distance
                    minIndex = k
            dp[j][i] = minDistance
            tracking[j][i] = minIndex

        
        elif i > j:
            dp[j][i] = dp[j][i - 1] + abs(police1Coordinate[i][0] - police1Coordinate[i - 1][0]) + abs(police1Coordinate[i][1] - police1Coordinate[i - 1][1])
            tracking[j][i] = i - 1

        
        elif i < j:
            dp[j][i] = dp[j - 1][i] + abs(police2Coordinate[j][0] - police2Coordinate[j - 1][0]) + abs(police2Coordinate[j][1] - police2Coordinate[j - 1][1])
            tracking[j][i] = j - 1


d = dp[0][-1]
minimumI = 0
flag = False
    
for i in range(1, len(police1Coordinate) - 1):
    if d > dp[i][-1]:
        d = dp[i][-1]
        minimumI = i
for i in range(1, len(police2Coordinate) - 1):
    if d > dp[-1][i]:
        d = dp[-1][i]
        minimumI = i
        flag = True
t = []

if flag:
   X = len(police2Coordinate) - 1
   Y = minimumI
   print(dp[-1][minimumI])
   for i in range(case):
       if X > Y:
           t.append(2)
           X = tracking[X][Y]
       elif X < Y:
           t.append(1)
           Y = tracking[X][Y]
                 
else:
    X = minimumI
    Y = len(police1Coordinate) - 1
    print(dp[minimumI][-1])
    for i in range(case):
       if X > Y:
           t.append(2)
           X = tracking[X][Y]
       elif X < Y:
           t.append(1)
           Y = tracking[X][Y]
 
for i in range(len(t)):
    print(t[len(t) - 1 - i]) 