import sys

input = sys.stdin.readline

N, M = map(int, input().split())
E = []
for i in range(N):
    E.append(int(input()))

E.sort()

proton = []
for i in range(M):
    proton.append(int(input()))

tree = [[] for i in range(E[-1] + 1)]
dp = [[0, 0] for i in range((E[-1] + 1))] 
for i in range(len(dp)):
   if i >= len(E):
       break
   dp[E[i]][1]  = E[i]



for i in range(len(proton)):
    for j in range(len(E)):
        if E[j] - proton[i] in E:
            tree[E[j]].append(E[j] - proton[i])
        if E[j] + proton[i] in E:
            tree[E[j]].append(E[j] + proton[i])
 

def DFS_DP(Tree, DP, node, visited = []):
    visited.append(node)
    for child in Tree[node]:
        if child in visited:
            continue
        DFS_DP(Tree, DP, child, visited)
        DP[node][0] += max(DP[child][0], DP[child][1])
        DP[node][1] += DP[child][0]
    
DFS_DP(tree, dp, E[0])
print(max(dp[E[0]][0], dp[E[0]][1]))