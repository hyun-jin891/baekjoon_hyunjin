from collections import deque

def bfs(graph, x, y):
    visited = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    need_v = deque()
    need_v.append([x, y])
    graph[y][x] = 0
    
    while need_v:
        start_x, start_y = need_v.popleft()
        visited.append([start_x, start_y])
        
        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= map_n or ny >= map_n:
                continue
            
            elif graph[ny][nx] == 1 and [nx, ny] not in visited:
                graph[ny][nx] = 0
                need_v.append([nx, ny])
                
    return len(visited)

map_n = int(input())
map = []
for n in range(map_n):
    prepare = []
    s = input()
    for i in s:
        prepare.append(int(i))
    map.append(prepare)

house_n = 0
output = []
for i in range(map_n):
    for j in range(map_n):
        if map[i][j] == 1:
            output.append(bfs(map, j, i))
            house_n += 1

print(house_n)
output.sort()
for o in output:
    print(o)