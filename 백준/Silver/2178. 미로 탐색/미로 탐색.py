from collections import deque
      
def bfs(graph, m, n, x=0, y=0):
    need_v = deque()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    need_v.append([x, y])
    distance = [[0]*m for i in range(n)]
    distance[0][0] = 1

    while need_v:
        start_x, start_y = need_v.popleft()
        if start_x == m-1 and start_y == n-1:
            return distance[start_y][start_x]
        
        for i in range(4):
            nx = start_x+dx[i]
            ny = start_y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            elif graph[ny][nx] == 1 and distance[ny][nx] == 0:
                need_v.append([nx, ny])
                distance[ny][nx] = distance[start_y][start_x] + 1
 
N, M = map(int, input().split())
arr = []
for n in range(N):
    prepare = [] 
    number = input()
    for num in number:
        prepare.append(int(num))
    arr.append(prepare)

print(bfs(arr, M, N))
        