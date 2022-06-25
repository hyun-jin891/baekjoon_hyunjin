from collections import deque
         
class Farm:
    def __init__(self, m, n):
        self.farm = []
        self.m = m
        self.n = n
        row = []
        for i in range(n):
            for j in range(m):
                row.append(0)
            self.farm.append(row)
            row = []
            
    def init_c(self, x, y):
        self.farm[y][x] = 1
        
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, a, b, m, n):
    q = deque()
    q.append((a, b))
    graph[b][a] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            elif graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny))
    return

test_n = int(input())
n = 0
output = []

while n < test_n:
    count_worm = 0
    M, N, K = map(int, input().split())
    f = Farm(M, N)
    for k in range(K):
        X, Y = map(int, input().split())
        f.init_c(X, Y)
    
    for i in range(N):
        for j in range(M):
            if f.farm[i][j] == 1:
                bfs(f.farm, j, i, M, N)
                count_worm += 1

    n += 1
    output.append(count_worm)

for i in output:
    print(i)
              