dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
M, N = map(int, input().split())
graph = [[0] * (N + 1)]
dp = [[0] * (N + 1) for i in range(M + 1)]

for i in range(M):
    l = [0]
    l.extend(list(map(int, input().split())))
    graph.append(l)

def DFS(graph, x, y, visited = []):
    count = 0
    visited.append((x, y))
    if x == N and y == M:
        dp[y][x] = 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 1 or nx > N or ny < 1 or ny > M:
            continue
        else:
            if graph[ny][nx] < graph[y][x]:
                if (nx, ny) in visited:
                    count += dp[ny][nx]
                else:
                    DFS(graph, nx, ny, visited)
                    count += dp[ny][nx]
                
    dp[y][x] = count

DFS(graph, 1, 1)
print(dp[1][1])