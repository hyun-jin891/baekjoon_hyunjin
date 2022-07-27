from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

def BFS(graph1, graph2, start_x, start_y):
    copyGraph1 = [l1[:] for l1 in graph1]
    copyGraph2 = [l2[:] for l2 in graph2]
    
    visited = deque()
    need_visit = deque() 
    need_visit.append((start_x, start_y))
    d = copyGraph2[start_y][start_x]
    
    while need_visit:
        x, y = need_visit.popleft()
        visited.append((x, y))
        data = copyGraph1[y][x]
        copyGraph1[y][x] = 0
        
        if copyGraph2[y][x] == d:
            copyGraph2[y][x] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= M or nx < 0 or ny >= N or ny < 0:
                continue
            
            if (nx, ny) not in visited and copyGraph1[ny][nx] == data:
                need_visit.append((nx, ny))
    
    if copyGraph1 == copyGraph2:
        return 1, visited
    else:
        return 0, visited
        
preGraph = [[0] * M for i in range(N)]
postGraph = [[0] * M for i in range(N)]

for i in range(N):
    a = input().split()
    for j in range(len(a)):
        preGraph[i][j] = int(a[j])

for i in range(N):
    a = input().split()
    for j in range(len(a)):
        postGraph[i][j] = int(a[j])

completeVisited = []
flag = False

for i in range(N):
    for j in range(M):
        if (j, i) in completeVisited:
            continue
        
        antibody, v = BFS(preGraph, postGraph, j, i)
        completeVisited.extend(v)
        
        if antibody == 1:
            flag = True
            break
        else:
            flag = False
    if flag:
        print("YES")
        break       
    
if not flag:
    print("NO")