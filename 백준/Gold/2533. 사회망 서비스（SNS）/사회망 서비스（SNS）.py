import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
tree = [[] for i in range(N + 1)]
dp = [[0, 1] for i in range(N + 1)]

for i in range(N - 1):
    node, nextNode = map(int, input().split())
    tree[node].append(nextNode)
    tree[nextNode].append(node)
visited = [0 for i in range(N + 1)]

def DFS_DP(n):
    global tree
    global visited
    global dp
    visited[n] = 1
    for child in tree[n]:
        if visited[child] == 1:
            continue
        DFS_DP(child)
        dp[n][0] += dp[child][1]
        dp[n][1] += min(dp[child][0], dp[child][1])



DFS_DP(1)
print(min(dp[1][0], dp[1][1]))