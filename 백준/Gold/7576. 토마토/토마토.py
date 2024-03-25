import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().split())
farm = []
dayGraph = [[-1 for i in range(M)] for i in range(N)]
start_tomatoes = []

for i in range(N):
    row = input().split()
    for j in range(M):
        if row[j] == "-1" or row[j] == "1":
            dayGraph[i][j] = 0
            if row[j] == "1":
                start_tomatoes.append((j, i))
    farm.append(row)
            
def BFS(graph, distance, start):
    #visited = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    need_v = deque(start)
    
    while need_v:
        x, y = need_v.popleft()
        #visited.append((x, y))
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                continue
            elif graph[next_y][next_x] == "-1" or graph[next_y][next_x] == "1":
                continue
            elif distance[next_y][next_x] != -1:
                continue
            else:
                need_v.append((next_x, next_y))
                distance[next_y][next_x] = distance[y][x] + 1


BFS(farm, dayGraph, start_tomatoes)

maximum = 0

for i in range(N):
    if -1 in dayGraph[i]:
        maximum = -1
        break
    if maximum < max(dayGraph[i]):
        maximum = max(dayGraph[i])

print(str(maximum))