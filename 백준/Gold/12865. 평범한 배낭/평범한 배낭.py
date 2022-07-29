N, K = map(int, input().split())
weightList = [0]
valueList = [0]

for i in range(1, N+1):
    w, v = map(int, input().split())
    weightList.append(w)
    valueList.append(v)

dp = [[0] * (K + 1) for i in range(N + 1)]

for i in range(1, len(dp)):
    for j in range(1, K + 1):
        if weightList[i] <= j:
            if valueList[i] + dp[i - 1][j - weightList[i]] > dp[i - 1][j]:
                dp[i][j] = valueList[i] + dp[i - 1][j - weightList[i]]
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] 

print(dp[N][K])