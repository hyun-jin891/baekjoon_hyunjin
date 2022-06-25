from collections import deque
def bfs(graph, start_node=1, visited=[]):
    need_v = deque()
    need_v.append(start_node)
    
    while need_v:
        node = need_v.popleft()
        visited.append(node)
        
        for i in range(len(graph)):
            if graph[node][i] == 1 and i not in visited:
                need_v.append(i)
    
    print(len(set(visited))-1)
            
num = int(input())
network = int(input())
matrix = [[0]*(num+1) for i in range(num+1)]
for n in range(network):
    node1, node2 = map(int, input().split())
    matrix[node1][node2] = matrix[node2][node1] = 1

bfs(matrix)